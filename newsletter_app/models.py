# Ce fichier définit les modèles de données pour l'application newsletter.
# Il contient la définition du modèle Subscriber qui représente un abonné à la newsletter.

from django.db import models  # Importation du module models de Django
from django.utils import timezone  # Importation du module timezone de Django

class Subscriber(models.Model):  # Définition du modèle Subscriber
    email = models.EmailField(unique=True)  # Champ email unique pour chaque abonné
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Date d'abonnement, ajoutée automatiquement

    def __str__(self):  # Méthode pour retourner une représentation en chaîne de caractères de l'objet
        return self.email  # Retourne l'email de l'abonné
