from . import views
from django.urls import path


app_name = 'register'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista_user/', views.lista_user, name='lista_user'),
    path("rederict/", views.rederict , name="rederict")
]
