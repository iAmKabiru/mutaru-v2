"""
WSGI config for pmp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""




import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pmp.settings')

application = get_wsgi_application()
application = WhiteNoise(application)



"""
import os
from whitenoise import WhiteNoise
from pmp import users

application = MyWSGIApp()
application = WhiteNoise(application, root='/path/users/static/')
application.add_files('/path/users/static/files', prefix='more-files/')
"""