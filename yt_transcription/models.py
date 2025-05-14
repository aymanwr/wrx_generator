from django.db import models

class Video(models.Model):
    url = models.URLField()
    transcription = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
