from . import views
from django.urls import path


app_name = 'register'
urlpatterns = [
    path('', views.index, name='home'),
    path('lista_user/', views.lista_user, name='lista_user'),
    path("rederict/", views.rederict , name="rederict"),
    path('perfil_user/', views.perfil_user, name='perfil_user'),
    path("register/", views.register, name="register"),
]
