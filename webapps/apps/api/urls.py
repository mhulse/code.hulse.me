from django.conf.urls.defaults import *
from piston.resource import Resource
from api.handlers import SnippetHandler
from api.emitters import ExtJSONEmitter

snippet_resource = Resource(handler=SnippetHandler)

urlpatterns = patterns('',
	
	url(r'', snippet_resource, name='api_url'),
	
)