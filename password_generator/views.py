# Importation des modules nécessaires
import random
import string
from django.shortcuts import render
from django.http import JsonResponse

# Fonction pour générer un mot de passe
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''  # Chaîne de caractères initiale vide
    if use_uppercase:
        characters += string.ascii_uppercase  # Ajoute les lettres majuscules si demandé
    if use_lowercase:
        characters += string.ascii_lowercase  # Ajoute les lettres minuscules si demandé
    if use_digits:
        characters += string.digits  # Ajoute les chiffres si demandé
    if use_special_chars:
        characters += string.punctuation  # Ajoute les caractères spéciaux si demandé

    if not characters:
        characters = string.ascii_letters + string.digits  # Par défaut, utilise les caractères alphanumériques

    # Génère le mot de passe en choisissant aléatoirement parmi les caractères disponibles
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Retourne le mot de passe généré

# Vue pour la page d'accueil
def index(request):
    return render(request, 'password_generator/index.html')  # Rend la page HTML de l'index

# Vue pour générer un mot de passe via une requête GET
def generate_password_view(request):
    if request.method == 'GET':  # Vérifie si la méthode de la requête est GET
        try:
            # Récupère les paramètres de la requête GET avec des valeurs par défaut
            password_length = int(request.GET.get('length', 12))  # Longueur par défaut du mot de passe est 12
            use_uppercase = bool(request.GET.get('uppercase', True))  # Utilise les majuscules par défaut
            use_lowercase = bool(request.GET.get('lowercase', True))  # Utilise les minuscules par défaut
            use_digits = bool(request.GET.get('digits', True))  # Utilise les chiffres par défaut
            use_special_chars = bool(request.GET.get('special_chars', True))  # N'utilise pas les caractères spéciaux par défaut

            # Génère le mot de passe avec les paramètres fournis
            password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special_chars)

            return JsonResponse({'password': password})  # Retourne le mot de passe généré en format JSON
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)  # Retourne une erreur en cas d'exception
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)  # Retourne une erreur si la méthode n'est pas GET
