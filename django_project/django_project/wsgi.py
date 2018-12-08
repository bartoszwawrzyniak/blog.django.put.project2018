"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/opt/djangostack-2.1.3-0/apps/django/django_projects/django_project')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/djangostack-2.1.3-0/apps/django/django_projects/django_project/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()
