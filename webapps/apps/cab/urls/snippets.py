from django.conf.urls.defaults import *
from cab.models import Snippet

urlpatterns = patterns('cab.views.snippets',
	
	url(r'^$', 'snippet_list', {}, name='cab_snippet_list'),
	url(r'^(?P<snippet_id>[a-zA-Z0-9]{6})/$', 'snippet_detail', {'template_name': 'cab/snippet_detail.html'}, name='cab_snippet_detail'),
	url(r'^(?P<snippet_id>[a-zA-Z0-9]{6})\.js$', 'snippet_detail', {'template_name': 'cab/snippet_detail_js.html', 'is_js': True}, name='cab_snippet_js'),
	url(r'^(?P<snippet_id>[a-zA-Z0-9]{6})\.txt', 'snippet_detail', {'template_name': 'cab/snippet_detail_raw.html', 'is_raw': True}, name='cab_snippet_raw'),
	url(r'^(?P<snippet_id>[a-zA-Z0-9]{6})\.embed', 'snippet_detail', {'template_name': 'cab/snippet_embed.html'}, name='cab_snippet_embed'),
	
)

urlpatterns += patterns('',
	
	url(r'^(?P<snippet_id>[a-zA-Z0-9]{6})\.(?P<emitter_format>.+)', include('api.urls')),
	
)