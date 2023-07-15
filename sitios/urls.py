from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bloque/<int:bloque_id>/', views.bloque, name='bloque'),
]