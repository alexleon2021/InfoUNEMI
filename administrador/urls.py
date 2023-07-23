from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.signout, name='logout'),
    path('registrarse', views.register, name='registrarse'),
    path('reestablecer', views.recuperarC, name='recuperarC'),
    path('administrador', views.administrador, name= 'administrador'),
    path('bloque/<int:bloque_id>/editar/', views.editar_bloque, name='editar_bloque'),
 ]