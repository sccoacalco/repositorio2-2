from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_post, name='crear_post'),
    path('exito/', views.post_exito, name='post_exito'),
]