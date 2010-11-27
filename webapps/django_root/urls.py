from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	
	(r'^admin/(.*)', admin.site.root),
	
#	(r'^code/', include('cab.urls.snippets')),
	
	url(r'^$', 'django_root.views.home', name='oontz_home'),
	
)
