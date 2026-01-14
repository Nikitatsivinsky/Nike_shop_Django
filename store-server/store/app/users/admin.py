from django.contrib import admin
from app.users.models import MailDistribution
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

admin.site.register(CustomUser)
admin.site.register(MailDistribution)