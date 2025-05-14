from django.urls import path, include
from . import views

app_name = 'password_generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_password', views.generate_password_view, name='generate_password'),
]
