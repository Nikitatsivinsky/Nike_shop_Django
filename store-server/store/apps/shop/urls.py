from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<int:category_id>/', views.CategorySortView.as_view(), name='category_sort'),
    path('category/<int:category_id>/<int:subcategory_id>/', views.SubCategorySortView.as_view(), name='category_sort'),
    path('category/<str:id>/', views.SingleProductView.as_view(), name='single_product'),
]