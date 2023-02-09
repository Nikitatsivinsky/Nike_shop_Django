"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import apps.shop.views as shop
import apps.auth.views as auth
import apps.orders.views as orders

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', shop.index, name='Main'),
    path('cart/', orders.cart, name='Cart'),
    path('category/', shop.category, name='Category'),
    path('checkout/', auth.checkout, name='Checkout'),
    path('confirmation/', orders.confirmation, name='Сonfirmation'),
    path('contact/', shop.contact, name='Сontact'),
    path('elements/', shop.elements, name='elements'),
    path('login/', auth.login, name='Login'),
    path('single-product/', shop.single_product, name='Single Product'),
    path('tracking/', orders.tracking, name='Tracking')
]
