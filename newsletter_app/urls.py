# Ce fichier définit les URL routes pour l'application newsletter.
# Il mappe les URLs aux vues correspondantes.

from django.urls import path
from . import views

app_name = 'newsletter_app'

urlpatterns = [
    path('', views.index, name='index'),  # Route pour la page d'accueil
    path('subscribe/', views.subscribe, name='subscribe'),  # Route pour s'abonner
]
