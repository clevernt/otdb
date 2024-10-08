"""
ASGI config for otdb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from servestatic import ServeStaticASGI

from django.core.asgi import get_asgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "otdb.settings")

application = get_asgi_application()
application = ServeStaticASGI(application, settings.STATIC_ROOT)
