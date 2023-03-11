from django.contrib import admin
from apps.auth.models import Profile, MailDistribution

admin.site.register(Profile)
admin.site.register(MailDistribution)