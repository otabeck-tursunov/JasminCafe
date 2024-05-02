from django.apps import AppConfig


class StatsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'statsApp'
    verbose_name = 'Buyurtmalar'

    def ready(self):
        import statsApp.models as models
