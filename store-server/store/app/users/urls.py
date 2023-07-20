from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('password/<int:pk>/', views.ChangePasswordView.as_view(), name='password'),

    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('confirm/<int:user_id>/', views.confirm_email, name='confirm_email'),




    # path('category/<int:category_id>/', views.CategorySortView.as_view(), name='category_sort'),
    # path('category/<int:category_id>/<int:subcategory_id>/', views.SubCategorySortView.as_view(), name='category_sort'),
    # path('category/<str:uuid>/', views.SingleProductView.as_view(), name='single_product'),
]