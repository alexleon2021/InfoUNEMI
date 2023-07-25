from django.urls import path
from . import views
from .views import MyPasswordResetView, MyPasswordResetDoneView,  MyPasswordResetConfirmView, MyPasswordResetCompleteView


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.signout, name='logout'),
    path('registrarse/', views.register, name='registrarse'),
    path('reset_recuperar/', views.recuperar, name='recuperar'),
    path('administrador/', views.administrador, name='administrador'),
    path('bloque/<int:bloque_id>/editar/', views.editar_bloque, name='editar_bloque'),

     ##Reestablecer contraseña
    path('reset/password_reset', MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/password_reset_done', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
