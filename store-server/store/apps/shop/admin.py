from apps.shop.models import Item, Application, Brand, Category, Color, Gender, Material, Type, Size, SubCategory, \
    MainBanner, NewesBanner, SaleBanner, ExclusiveBanner, PopularBanner
from django.contrib import admin


@admin.register(Item)
class MyModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('materials', 'applications', 'colors', 'types', 'size', 'subcategory')


admin.site.register(Size)
admin.site.register(SubCategory)
admin.site.register(Application)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(Material)
admin.site.register(Type)
admin.site.register(MainBanner)
admin.site.register(NewesBanner)
admin.site.register(SaleBanner)
admin.site.register(ExclusiveBanner)
admin.site.register(PopularBanner)

