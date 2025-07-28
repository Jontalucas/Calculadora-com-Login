from django.urls import path
from . import views

app_name = 'calculadora'
urlpatterns = [
    path('', views.Calculadora, name = 'Calculadora'),
    path('logout', views.Logout, name = 'Logout'),
]
