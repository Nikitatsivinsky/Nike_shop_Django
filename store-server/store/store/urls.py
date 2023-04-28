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
from django.conf.urls.static import static
from django.conf import settings

import apps.shop.views as shop
import apps.auth.views as auth
import apps.orders.views as orders
import apps.other.views as other

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('', shop.index, name='index'),
    path('cart/', orders.cart, name='basket'),
    path('category/', shop.category, name='category'),
    path('checkout/', auth.checkout, name='checkout'),
    path('confirmation/', orders.confirmation, name='conformation'),
    path('contact/', other.contact, name='contact'),
    path('elements/', other.elements, name='elements'),
    path('login/', auth.login, name='login'),
    path('single-product/', shop.single_product, name='single_product'),
    path('tracking/', orders.tracking, name='tracking'),
    path('registration/', auth.registration, name='registration'),
    path('profile/', auth.profile, name='profile'),
]

# add url for site_images folder
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
