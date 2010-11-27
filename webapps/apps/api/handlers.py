from piston.handler import AnonymousBaseHandler
from cab.models import Snippet

class SnippetHandler(AnonymousBaseHandler):
	
	model = Snippet
#	anonymous = 'AnonymousSnippetHandler'
	fields = (
		#'secret_id',
		#'title',
		#'published',
		#'updated',
		#('author', ('username',)),
		#('language', ('slug', 'name',)),
		#'description',
		#'description_html',
		#'code',
		'code_highlighted',
	)
	methods_allowed = ('GET',)
	
	def read(self, request, snippet_id=None):
		base = Snippet.objects
		if snippet_id:
			return base.get(sid=snippet_id)
		else:
			return base.live()

"""
class AnonymousSnippetHandler(SnippetHandler, AnonymousBaseHandler):
	fields = (
		'pub_date',
		'updated_date',
		'language',
		'description_html',
		'highlighted_code',
	)
"""
