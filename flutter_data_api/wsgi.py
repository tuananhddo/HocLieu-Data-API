"""
WSGI config for flutter_data_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flutter_data_api.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'flutter_data_api.settings'
# application = get_wsgi_application()
application = DjangoWhiteNoise(get_wsgi_application())
