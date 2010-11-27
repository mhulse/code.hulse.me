import urlparse
from django.template import Library
from django.template.defaulttags import URLNode, url
from django.contrib.sites.models import Site

register = Library()

class AbsoluteURLNode(URLNode):
	def render(self, context):
		path = super(AbsoluteURLNode, self).render(context)
		domain = "http://%s" % Site.objects.get_current().domain
		if self.asvar:
			context[self.asvar]= urlparse.urljoin(domain, context[self.asvar])
			the_return = ''
		else:
			the_return = urlparse.urljoin(domain, path)
		return the_return

def absurl(parser, token, node_cls=AbsoluteURLNode):
	"""Just like {% url %} but ads the domain of the current site."""
	node_instance = url(parser, token)
	return node_cls(
		view_name=node_instance.view_name,
		args=node_instance.args,
		kwargs=node_instance.kwargs,
		asvar=node_instance.asvar
	)
absurl = register.tag(absurl)
