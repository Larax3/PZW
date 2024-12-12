from django.urls import path
from django.contrib.auth import views as auth_views
from PZWapp import views

app_name = 'PZWapp'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('', views.homepage, name='homepage'),
]