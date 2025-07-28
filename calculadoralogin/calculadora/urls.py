from django.urls import path
from .views import calculadora_view

app_name = 'calculadora'

urlpatterns = [
    path('', calculadora_view, name='calculadora'),
]
