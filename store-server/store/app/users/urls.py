from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    # path('category/<int:category_id>/', views.CategorySortView.as_view(), name='category_sort'),
    # path('category/<int:category_id>/<int:subcategory_id>/', views.SubCategorySortView.as_view(), name='category_sort'),
    # path('category/<str:uuid>/', views.SingleProductView.as_view(), name='single_product'),
]