from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('password/<int:pk>/', views.ChangePasswordView.as_view(), name='password'),

    # path('category/<int:category_id>/', views.CategorySortView.as_view(), name='category_sort'),
    # path('category/<int:category_id>/<int:subcategory_id>/', views.SubCategorySortView.as_view(), name='category_sort'),
    # path('category/<str:uuid>/', views.SingleProductView.as_view(), name='single_product'),
]