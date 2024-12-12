from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PZWapp.urls')),  # Povezivanje aplikacije s glavnim URL-ovima
]