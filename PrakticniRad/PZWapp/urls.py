from django.urls import path,include
from django.contrib.auth import views as auth_views
from PZWapp import views
from .views import (
    VrtnaBiljkaListView, VrtnaBiljkaDetailView, 
    PovrtnaBiljkaListView, PovrtnaBiljkaDetailView,
    VrtnaBiljkaCreateView, VrtnaBiljkaUpdateView, VrtnaBiljkaDeleteView,
    PovrtnaBiljkaCreateView, PovrtnaBiljkaUpdateView, PovrtnaBiljkaDeleteView,
    register, admin_view, delete_user, homepage
)
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from .views import PovrtnaBiljkaViewSet, VrtnaBiljkaViewSet

app_name = 'PZWapp'

router = DefaultRouter()
router.register(r'povrtne-biljke', PovrtnaBiljkaViewSet)
router.register(r'vrtne-biljke', VrtnaBiljkaViewSet)
# URL-ovi za autentikaciju
auth_urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

# URL-ovi za administraciju
admin_urlpatterns = [
    path('admin_view/', views.admin_view, name='admin_view'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
]

# URL-ovi za VrtnaBiljka
vrtna_biljka_urlpatterns = [
    path('vrtnabiljke/', VrtnaBiljkaListView.as_view(), name='vrtnabiljka_list'),
    path('vrtnabiljke/<int:pk>/', VrtnaBiljkaDetailView.as_view(), name='vrtnabiljka_detail'),
    path('vrtnabiljke/dodaj/', VrtnaBiljkaCreateView.as_view(), name='vrtnabiljka_create'),
    path('vrtnabiljke/<int:pk>/uredi/', VrtnaBiljkaUpdateView.as_view(), name='vrtnabiljka_update'),
    path('vrtnabiljke/<int:pk>/obrisi/', VrtnaBiljkaDeleteView.as_view(), name='vrtnabiljka_delete'),
]

# URL-ovi za PovrtnaBiljka
povrtna_biljka_urlpatterns = [
    path('povrtnabiljke/', PovrtnaBiljkaListView.as_view(), name='povrtnabiljka_list'),
    path('povrtnabiljke/<int:pk>/', PovrtnaBiljkaDetailView.as_view(), name='povrtnabiljka_detail'),
    path('povrtnabiljke/dodaj/', PovrtnaBiljkaCreateView.as_view(), name='povrtnabiljka_create'),
    path('povrtnabiljke/<int:pk>/uredi/', PovrtnaBiljkaUpdateView.as_view(), name='povrtnabiljka_update'),
    path('povrtnabiljke/<int:pk>/obrisi/', PovrtnaBiljkaDeleteView.as_view(), name='povrtnabiljka_delete'),
]

# Ostali URL-ovi
other_urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('', include(router.urls)), 
]

# Kombiniranje svih URL-ova
urlpatterns = (
    auth_urlpatterns +
    admin_urlpatterns +
    vrtna_biljka_urlpatterns +
    povrtna_biljka_urlpatterns +
    other_urlpatterns
)

# Dodavanje URL-ova za statičke datoteke u debug modu
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)