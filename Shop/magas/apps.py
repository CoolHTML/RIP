from django.apps import AppConfig


class MagasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'magas'

    def ready(self):
        import magas.signals
