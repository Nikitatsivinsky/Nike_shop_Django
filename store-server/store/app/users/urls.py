from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('password/<int:pk>/', views.ChangePasswordView.as_view(), name='password'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('category/<int:category_id>/', views.CategorySortView.as_view(), name='category_sort'),
    # path('category/<int:category_id>/<int:subcategory_id>/', views.SubCategorySortView.as_view(), name='category_sort'),
    # path('category/<str:uuid>/', views.SingleProductView.as_view(), name='single_product'),
]