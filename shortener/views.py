from django.shortcuts import render, redirect  # Importation des fonctions render et redirect pour rendre des templates et rediriger les requêtes
from .models import Link  # Importation du modèle Link
import random  # Importation du module random pour générer des valeurs aléatoires
import string  # Importation du module string pour manipuler des chaînes de caractères
from django.http import HttpResponse  # Importation de HttpResponse pour envoyer des réponses HTTP

def index(request):
    short_url = None  # Initialise short_url à None
    if request.method == 'POST':  # Vérifie si la méthode de la requête est POST
        original_url = request.POST.get('original_url')  # Récupère l'URL originale du formulaire
        existing_link = Link.objects.filter(original_url=original_url).first()  # Cherche un lien existant avec la même URL originale
        if existing_link:  # Si un lien existe déjà
            short_url = request.build_absolute_uri(existing_link.get_short_url())  # Construit l'URL courte existante
        else:
            link = Link(original_url=original_url)  # Crée un nouvel objet Link avec l'URL originale
            link.save()  # Sauvegarde le nouvel objet Link dans la base de données
            short_url = request.build_absolute_uri(link.get_short_url())  # Construit l'URL courte pour le nouveau lien
    return render(request, 'shortener/index.html', {'short_url': short_url})  # Rend le template index.html avec l'URL courte

def redirect_original(request, short_code):
    link = Link.objects.get(short_url=short_code)  # Récupère le lien correspondant au code court
    return redirect(link.original_url)  # Redirige vers l'URL originale

def generate_short_url():
    characters = string.ascii_letters + string.digits  # Ensemble de caractères possibles (lettres et chiffres)
    short_url = ''.join(random.choice(characters) for _ in range(8))  # Génère une chaîne de 6 caractères aléatoires
    return short_url  # Retourne l'URL courte générée

