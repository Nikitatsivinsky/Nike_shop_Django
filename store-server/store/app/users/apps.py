from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    label = "custom_user"
    name = 'app.users'
    verbose_name = 'Користувачі'
    # default = False