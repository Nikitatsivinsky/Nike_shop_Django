from django.apps import AppConfig

class OtherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = "other"
    name = 'app.other'
    verbose_name = 'Налаштування сайту'