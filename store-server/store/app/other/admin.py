from django.contrib import admin
from .models import MainBanner,NewesBanner,SaleBanner,ExclusiveBanner,PopularBanner


admin.site.register(MainBanner)
admin.site.register(NewesBanner)
admin.site.register(SaleBanner)
admin.site.register(ExclusiveBanner)
admin.site.register(PopularBanner)