from django.urls import path
from . import views

app_name = 'shortener'

urlpatterns = [
    path('', views.index, name='index'),  # Route pour la page d'accueil, associée à la vue index
    path('<str:short_code>/', views.redirect_original, name='redirect_original_url'),  # Route pour rediriger vers l'URL originale, associée à la vue redirect_original
    # <str:short_code> capture une chaîne de caractères depuis l'URL et la passe en tant que paramètre nommé 'short_code' à la vue
]
