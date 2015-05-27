from django.apps import AppConfig
from django.db.models.signals import post_migrate

from .management import create_backends
from .management import create_notifications


class NotifierConfig(AppConfig):
    name = 'notifier'
    verbose_name = 'Notifier'

    def ready(self):
        post_migrate.connect(create_backends, sender=self)
        post_migrate.connect(create_notifications, sender=self)
