from django.apps import AppConfig


class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'
    verbose_name = 'Journal des actions'

    def ready(self):
        # Enregistrer les exclusions par défaut
        from .registry import ActionLogRegistry
        ActionLogRegistry.register_default_exclusions()

        # Importer les signaux pour les connecter
        from . import signals  # noqa
