from django.core.management.base import BaseCommand  # Importation de la classe de base pour les commandes de gestion Django
from django.core.mail import send_mail  # Importation de la fonction pour envoyer des emails
from newsletter_app.models import Subscriber  # Importation du modèle Subscriber

class Command(BaseCommand):  # Définition d'une nouvelle commande de gestion
    help = 'Send newsletters to all subscribers'  # Description de l'aide pour cette commande

    def handle(self, *args, **kwargs):  # Méthode principale exécutée lors de l'appel de la commande
        subscribers = Subscriber.objects.all()  # Récupération de tous les abonnés
        for subscriber in subscribers:  # Boucle sur chaque abonné
            send_mail(
                'Newsletter Subject',  # Sujet de l'email
                'Here is the message content of the newsletter.',  # Contenu du message de la newsletter
                'WRX-Generator@gmail.com',  # Adresse email de l'expéditeur
                [subscriber.email],  # Liste des destinataires (un seul destinataire ici)
                fail_silently=False,  # Lever une exception en cas d'échec de l'envoi
            )
        self.stdout.write(self.style.SUCCESS('Successfully sent newsletters'))  # Affichage d'un message de succès dans la console

