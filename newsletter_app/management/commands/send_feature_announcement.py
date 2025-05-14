from django.core.management.base import BaseCommand  # Importation de la classe de base pour les commandes de gestion Django
from django.core.mail import EmailMessage  # Importation de la classe pour envoyer des emails
from django.template.loader import render_to_string  # Importation de la fonction pour rendre un template en chaîne de caractères
from newsletter_app.models import Subscriber  # Importation du modèle Subscriber

class Command(BaseCommand):  # Définition d'une nouvelle commande de gestion
    help = 'Send feature announcement emails to all subscribers'  # Description de l'aide pour cette commande

    def handle(self, *args, **kwargs):  # Méthode principale exécutée lors de l'appel de la commande
        subscribers = Subscriber.objects.all()  # Récupération de tous les abonnés
        for subscriber in subscribers:  # Boucle sur chaque abonné
            subject = 'Découvrez notre nouvelle fonctionnalité : QR Code Generator !'  # Sujet de l'email
            html_content = render_to_string('newsletter_app/feature_announcement_email.html', {'email': subscriber.email})  # Rendu du contenu HTML de l'email avec le template
            from_email = 'WRX-Generator@gmail.com'  # Adresse email de l'expéditeur

            recipient_list = [subscriber.email]  # Liste des destinataires (un seul destinataire ici)

            email_message = EmailMessage(subject, html_content, from_email, recipient_list)  # Création de l'objet email
            email_message.content_subtype = 'html'  # Définition du type de contenu comme HTML
            email_message.send()  # Envoi de l'email

            self.stdout.write(self.style.SUCCESS(f'Successfully sent feature announcement email to {subscriber.email}'))  # Affichage d'un message de succès dans la console

