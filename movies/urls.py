from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('red/', views.red, name='red'),
]
