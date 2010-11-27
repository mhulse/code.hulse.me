import datetime
import random
from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import _get_queryset
from cab.highlight import pygmentize, LEXER_ALL, LEXER_CODE

t = 'abcdefghijkmnopqrstuvwwxyzABCDEFGHIJKLOMNOPQRSTUVWXYZ1234567890'
def generate_sid(length=6):
	return ''.join([random.choice(t) for i in range(length)])

def get_object_or_None(klass, *args, **kwargs):
	queryset = _get_queryset(klass)
	try:
		return queryset.get(*args, **kwargs)
	except queryset.model.DoesNotExist:
		return None

class Language(models.Model):
	
	name = models.CharField(_(u'Language'), max_length=100, choices=LEXER_ALL)
	slug = models.SlugField(_(u'Slug'), unique=True)
	language_code = models.CharField(_(u'Language Code'), max_length=50, choices=LEXER_CODE)
	
	class Meta:
		ordering = ['name']
	
	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('cab_language_detail', (), { 'slug': self.slug })

class LiveSnippetManager(models.Manager):
	def get_query_set(self):
		return super(LiveSnippetManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)

class Snippet(models.Model):
	
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
	)
	
	sid = models.CharField(_(u'Secret ID'), max_length=6, editable=False)
	title = models.CharField(_(u'Title'), max_length=255, blank=True)
	author = models.ForeignKey(User)
	code = models.TextField(_(u'Code'), )
	code_highlighted = models.TextField(_(u'Highlighted Code'), editable=False)
	language = models.ForeignKey(Language)
	description = models.TextField(_(u'Description'), blank=True)
	description_html = models.TextField(_(u'HTML Description'), editable=False)
	published = models.DateTimeField(_(u'Published'), editable=False)
	updated = models.DateTimeField(_(u'Updated'), editable=False)
	status = models.IntegerField(_(u'Status'), choices=STATUS_CHOICES, default=LIVE_STATUS)
	
	# Need to be this way around so that non-live entries will show up in Admin, which uses the default (first) manager.
	objects = models.Manager()
	live = LiveSnippetManager()
	
	class Meta:
		ordering = ['-published']
	
	def line_count(self):
		return range(len(self.code.splitlines()))

	def code_splitted(self):
		return self.code_highlighted.splitlines()
	
	def is_modified(self):
		# Comparing timestamps:
		# http://snipurl.com/x66el
		second = datetime.timedelta(seconds=1)
		delta = self.updated - self.published
		return delta >= second
	
	def save(self, *args, **kwargs):
		if not self.pk:
			self.published = datetime.datetime.now()
			self.sid = generate_sid()
			while get_object_or_None(Snippet, sid=self.sid) != None:
				self.sid = generate_sid()
		self.updated = datetime.datetime.now()
		self.description_html = markdown(self.description)
		self.code = self.code.strip()
		self.code_highlighted = pygmentize(self.code.expandtabs(4), self.language.language_code)
		super(Snippet, self).save(*args, **kwargs)
	
	@models.permalink
	def get_absolute_url(self):
		return ('cab_snippet_detail', (self.sid,))
	
	def __unicode__(self):
		return '%s' % self.sid
