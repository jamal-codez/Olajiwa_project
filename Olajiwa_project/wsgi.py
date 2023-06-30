"""
WSGI config for Olajiwa_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

#!\Users\Jamal\Desktop\venv1 python
import os
import sys 

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Olajiwa_project.settings')

application = get_wsgi_application()
app=application
