# Ce fichier définit les vues pour l'application newsletter.
# Il contient les fonctions de vue pour gérer les abonnements et les désabonnements.

from django.shortcuts import render, redirect  # Importation des fonctions pour rendre des templates et rediriger des URLs
from django.http import JsonResponse  # Importation de la classe JsonResponse pour les réponses JSON
from django.core.mail import EmailMessage  # Importation de la classe EmailMessage pour envoyer des emails
from django.template.loader import render_to_string  # Importation de la fonction render_to_string pour rendre des templates en chaîne de caractères
from django.contrib import messages  # Importation du module messages pour afficher des messages à l'utilisateur
from django.db import IntegrityError  # Importation de l'exception IntegrityError pour gérer les erreurs d'intégrité de la base de données
from django.views.decorators.csrf import csrf_exempt  # Importation du décorateur csrf_exempt pour désactiver la protection CSRF pour une vue
from .models import Subscriber  # Importation du modèle Subscriber

@csrf_exempt  # Exemption de la vérification CSRF pour cette vue
def index(request):  # Vue pour afficher la page d'accueil
    return render(request, 'newsletter_app/index.html')  # Rendre le template index.html

def subscribe(request):  # Vue pour gérer les abonnements
    if request.method == "POST":  # Si la méthode de la requête est POST
        email = request.POST.get('email')  # Récupérer l'email d'u formulaire


        if email:  # Si un email est fourni
            try:
                Subscriber.objects.create(email=email)  # Créer un nouvel abonné avec l'email fourni
                subject = 'Subscription Confirmation'  # Sujet de l'email de confirmation
                html_content = render_to_string('newsletter_app/welcome_email.html', {'email': email})  # Rendre le contenu HTML de l'email avec le template
                from_email = 'WRX-Generator@gmail.com'  # Adresse email de l'expéditeur
                recipient_list = [email]  # Liste des destinataires (un seul destinataire ici)
                email_message = EmailMessage(subject, html_content, from_email, recipient_list)  # Création de l'objet email
                email_message.content_subtype = 'html'  # Définition du type de contenu comme HTML
                email_message.send()  # Envoi de l'email
                response = {
                    'status': 'success',
                    'message': 'You have successfully subscribed to the newsletter and a confirmation email has been sent!'
                }
                return JsonResponse(response)  # Retourner une réponse JSON de succès
            except IntegrityError:  # Si une erreur d'intégrité se produit (par exemple, email déjà abonné)
                response = {
                    'status': 'error',
                    'message': 'This email is already subscribed.'
                }
                return JsonResponse(response)  # Retourner une réponse JSON d'erreur
        else:  # Si aucun email n'est fourni
            response = {
                'status': 'error',
                'message': 'Please enter a valid email address.'
            }
            return JsonResponse(response)  # Retourner une réponse JSON d'erreur
    else:  # Si la méthode de la requête n'est pas POST
        response = {
            'status': 'error',
            'message': 'Invalid request method.'
        }
        return JsonResponse(response)  # Retourner une réponse JSON d'erreur

