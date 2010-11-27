import os
import sys

sys.path = [
    '/home/mhulse/webapps/django',
    '/home/mhulse/webapps/django/lib/python2.5/',
    '/home/mhulse/webapps/django/lib/python2.5/django-trunk/django',
    # Keep above. Added:
    #'/home/mhulse/webapps/django',
    '/home/mhulse/webapps/django/apps',
    '/home/mhulse/webapps/django/django_root',
] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_root.settings'
application = WSGIHandler()
