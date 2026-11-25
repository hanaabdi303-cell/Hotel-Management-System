from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='hotel/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard URL
    path('', views.dashboard, name='dashboard'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:id>/', views.category_delete, name='category_delete'),

    # Room URLs
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.room_add, name='room_add'),
    path('rooms/edit/<int:id>/', views.room_edit, name='room_edit'),
    path('rooms/delete/<int:id>/', views.room_delete, name='room_delete'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.customer_add, name='customer_add'),
    path('customers/edit/<int:id>/', views.customer_edit, name='customer_edit'),
    path('customers/delete/<int:id>/', views.customer_delete, name='customer_delete'),

    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.reservation_add, name='reservation_add'),
    path('reservations/checkin/<int:id>/', views.reservation_checkin, name='reservation_checkin'),
    path('reservations/checkout/<int:id>/', views.reservation_checkout, name='reservation_checkout'),
]