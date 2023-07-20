from django.contrib import admin
from app.orders.models import Order, Cart

admin.site.register(Order)
admin.site.register(Cart)
