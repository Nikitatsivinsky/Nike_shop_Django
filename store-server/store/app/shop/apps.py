from django.apps import AppConfig


class ShopConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = "shop"
    name = 'app.shop'
    verbose_name = 'Магазин'

