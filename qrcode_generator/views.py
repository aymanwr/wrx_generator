import qrcode  # Importation de la bibliothèque qrcode pour générer des QR codes
from django.http import HttpResponse  # Importation de HttpResponse pour envoyer des réponses HTTP
from io import BytesIO  # Importation de BytesIO pour manipuler des flux de données en mémoire
from django.shortcuts import render  # Importation de render pour rendre des templates
import base64  # Importation de base64 pour encoder des données en base64
from PIL import Image  # Importation de PIL (Pillow) pour manipuler des images

def index(request):
    return render(request, 'qrcode_generator/index.html')  # Rend le template index.html pour la vue d'index

def generate_qr_code(request):
    # Extraction des données des paramètres de la requête URL
    data = request.GET.get('url', '')  # Récupère la valeur du paramètre 'url' ou une chaîne vide par défaut
    style_option = request.GET.get('style_option', 'black_on_white')  # Récupère la valeur du paramètre 'style_option' ou 'black_on_white' par défaut

    # Définition des couleurs en fonction de l'option sélectionnée
    if style_option == 'black_on_white':
        fill_color = 'black'  # Couleur de remplissage noire
        back_color = 'white'  # Couleur de fond blanche
    elif style_option == 'white_on_black':
        fill_color = 'white'  # Couleur de remplissage blanche
        back_color = 'black'  # Couleur de fond noire
    elif style_option == 'black_transparent':
        fill_color = 'black'  # Couleur de remplissage noire
        back_color = None  # Pas de couleur de fond (transparent)
    elif style_option == 'white_transparent':
        fill_color = (255,255,250)  # Couleur de remplissage blanche
        back_color = None  # Pas de couleur de fond (transparent)



    # Création d'un objet BytesIO pour stocker l'image du QR code
    qr_code_image = BytesIO()

    # Génération du QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)  # Création d'un objet QRCode avec des paramètres spécifiques
    qr.add_data(data)  # Ajout des données au QR code
    qr.make(fit=True)  # Ajustement du QR code pour qu'il tienne dans l'espace disponible

    # Création de l'image du QR code
    if back_color is not None:
        img = qr.make_image(fill_color=fill_color, back_color=back_color)  # Création de l'image avec les couleurs spécifiées
    else:
        # Création d'une image avec un fond blanc d'abord
        img = qr.make_image(fill_color=fill_color, back_color="white").convert("RGBA")  # Conversion en mode RGBA pour la transparence
        datas = img.getdata()  # Récupération des données de l'image
        new_data = []
        for item in datas:
            # Conversion du fond blanc en transparent
            if item[:3] == (255, 255, 255):
                new_data.append((255, 255, 255, 0))  # Ajout d'un pixel transparent
            else:
                new_data.append(item)  # Ajout du pixel original
        img.putdata(new_data)  # Mise à jour des données de l'image
        
        if fill_color == 'white':
            # Remplacement du QR code noir par un QR code blanc
            datas = img.getdata()  # Récupération des données de l'image
            new_data = []
            for item in datas:
                if item[:3] == (0, 0, 0):
                    new_data.append((255, 255, 255, 255))  # Remplacement du noir par du blanc
                else:
                    new_data.append(item)  # Ajout du pixel original
            img.putdata(new_data)  # Mise à jour des données de l'image

    img.save(qr_code_image, format='PNG')  # Sauvegarde de l'image dans l'objet BytesIO au format PNG

    # Préparation de l'image pour l'affichage
    qr_code_image.seek(0)  # Remise à zéro du pointeur de l'objet BytesIO
    base64_image = base64.b64encode(qr_code_image.getvalue()).decode('utf-8')  # Encodage de l'image en base64

    # Passage de l'image à un nouveau template pour l'affichage
    context = {
        'base64_image': base64_image,  # Image encodée en base64
        'file_format': 'png'  # Format du fichier
    }
    return render(request, 'qrcode_generator/display.html', context)  # Rend le template display.html avec le contexte
