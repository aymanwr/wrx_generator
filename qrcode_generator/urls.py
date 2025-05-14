# qrcode_generator/urls.py

from django.urls import path  # Importation de la fonction path pour définir les routes URL
from . import views  # Importation des vues de l'application qrcode_generator

app_name = 'qrcode_generator'  # Définition du nom de l'application pour les espaces de noms des URL

urlpatterns = [
    path('', views.index, name='index'),  # Route pour la page d'accueil, associée à la vue index
    path('generate_qr_code/', views.generate_qr_code, name='generate_qr_code'),  # Route pour générer un QR code, associée à la vue generate_qr_code
]
