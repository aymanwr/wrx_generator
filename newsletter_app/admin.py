# Ce fichier enregistre le modèle Subscriber dans l'interface d'administration de Django.
# Cela permet de gérer les abonnés via l'interface d'administration.

from django.contrib import admin  # Importation du module admin de Django
from .models import Subscriber  # Importation du modèle Subscriber

admin.site.register(Subscriber)  # Enregistrement du modèle Subscriber dans l'interface d'administration
