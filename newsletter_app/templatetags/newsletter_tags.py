# Ce fichier définit un tag de template personnalisé pour l'application newsletter.
# Il permet d'inclure un formulaire d'abonnement dans les templates Django en utilisant le tag d'inclusion 'show_subscription_form'.

from django import template  # Importation du module template de Django
from django.urls import reverse  # Importation de la fonction reverse pour obtenir des URLs à partir de noms de vues

register = template.Library()  # Création d'une instance de la bibliothèque de templates

@register.inclusion_tag('newsletter_app/subscribe_form.html', takes_context=True)  # Déclaration d'un tag d'inclusion avec le template spécifié
def show_subscription_form(context):  # Définition de la fonction pour afficher le formulaire d'abonnement
    return {
        'request': context['request'],  # Retourne le contexte avec l'objet request
    }
