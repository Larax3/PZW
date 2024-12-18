from django.urls import path
from django.contrib.auth import views as auth_views
from PZWapp import views
from .views import (
    VrtnaBiljkaListView, VrtnaBiljkaDetailView, 
    PovrtnaBiljkaListView, PovrtnaBiljkaDetailView
)

app_name = 'PZWapp'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('', views.homepage, name='homepage'),
    path('vrtnabiljke/', VrtnaBiljkaListView.as_view(), name='vrtnabiljka_list'),
    path('vrtnabiljke/<int:pk>/', VrtnaBiljkaDetailView.as_view(), name='vrtnabiljka_detail'),
    path('povrtnabiljke/', PovrtnaBiljkaListView.as_view(), name='povrtnabiljka_list'),
    path('povrtnabiljke/<int:pk>/', PovrtnaBiljkaDetailView.as_view(), name='povrtnabiljka_detail'),
]