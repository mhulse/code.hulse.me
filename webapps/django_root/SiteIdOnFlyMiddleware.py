from django.conf import settings

class SiteIdOnFlyMiddleware:
	def process_request(self, request):
		host = request.META.get('HTTP_HOST')
		
		if 'code.hulse.me' in host:
			settings.SITE_ID = 2
		else:
			settings.SITE_ID = 1
