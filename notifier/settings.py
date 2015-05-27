###############################################################################
# Imports
###############################################################################
# Python
from importlib import import_module

# Django
from django.conf import settings


###############################################################################
# App Settings
###############################################################################
BACKENDS = getattr(
    settings,
    'NOTIFIER_BACKENDS',
    ('notifier.backends.EmailBackend',)
)

# By default, we'll look in the <app>.notifications module to create any
# app-specific notifications. Override this in your settings module to
# look elsewhere
AUTO_CREATE_MODULE_NAME = getattr(
    settings,
    'NOTIFIER_AUTO_CREATE_MODULE_NAME',
    'notifications'
)

BACKEND_CLASSES = [
    getattr(import_module(mod), cls)
    for (mod, cls) in (backend.rsplit(".", 1)
    for backend in BACKENDS)
]

# Whether or not to record SentNotification objects
# Not doing so can improve performance, but also lets you store your
# own
CREATE_SENT_NOTIFICATIONS = getattr(
    settings,
    'NOTIFIER_CREATE_SENT_NOTIFICATIONS',
    True
)
