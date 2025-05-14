# newsletter_app/management/commands/delete_subscribers.py

from django.core.management.base import BaseCommand  # Importe BaseCommand de Django pour créer des commandes personnalisées
from newsletter_app.models import Subscriber  # Importe le modèle Subscriber depuis l'application newsletter_app

class Command(BaseCommand):  # Définit une nouvelle commande en héritant de BaseCommand
    help = 'Deletes all subscribers from the database'  # Texte d'aide qui décrit ce que fait la commande

    def handle(self, *args, **kwargs):  # La méthode handle est appelée quand la commande est exécutée
        # self fait référence à l'instance actuelle de la classe Command
        # *args permet de capturer un nombre variable d'arguments positionnels
        # **kwargs permet de capturer un nombre variable d'arguments nommés
        subscribers_count = Subscriber.objects.count()  # Compte le nombre total d'abonnés dans la base de données
        Subscriber.objects.all().delete()  # Supprime tous les abonnés de la base de données
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {subscribers_count} subscribers'))  # Affiche un message de succès avec le nombre d'abonnés supprimés

