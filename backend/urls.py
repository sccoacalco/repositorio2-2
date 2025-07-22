from django.contrib import admin
from django.urls import path, include, re_path
from loginapp.views import FrontendAppView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginapp.urls')),  # Ahora las rutas están en raíz
    re_path(r'^.*$', FrontendAppView.as_view(), name='frontend'),
]