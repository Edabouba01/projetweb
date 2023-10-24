"""
ASGI config for projetweb project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetweb.settings")

application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from yourapp.routing import websocket_urlpatterns  # Assurez-vous d'importer correctement vos routes

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
        # D'autres routeurs pour d'autres protocoles (HTTP, etc.) peuvent être ajoutés ici
    }
)
