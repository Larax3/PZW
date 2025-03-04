from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PZWapp.urls')), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', include('PZWapp.urls')),
]