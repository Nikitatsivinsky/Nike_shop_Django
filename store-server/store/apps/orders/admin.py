from django.contrib import admin
from apps.orders.models import Order, Cart

admin.site.register(Order)
admin.site.register(Cart)
