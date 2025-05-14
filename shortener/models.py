from django.db import models  # Importation du module models de Django pour définir des modèles de base de données
import shortuuid  # Importation de la bibliothèque shortuuid pour générer des identifiants uniques courts

class Link(models.Model):
    original_url = models.URLField(unique=True)  # Champ pour stocker l'URL originale, doit être unique
    short_url = models.CharField(max_length=100, unique=True)  # Champ pour stocker l'URL courte, doit être unique

    def save(self, *args, **kwargs):  # Redéfinition de la méthode save
        # self : référence à l'instance actuelle de la classe
        # *args : permet de passer un nombre variable d'arguments positionnels à la méthode
        # **kwargs : permet de passer un nombre variable d'arguments nommés à la méthode
        if not self.pk:  # Vérifie si l'objet n'a pas encore été sauvegardé dans la base de données
            self.short_url = shortuuid.uuid()[:8]  # Génère un identifiant unique court de 8 caractères pour l'URL courte
        super().save(*args, **kwargs)  # Appelle la méthode save() de la classe parente pour sauvegarder l'objet

    def get_short_url(self):
        return self.short_url  # Retourne l'URL courte
