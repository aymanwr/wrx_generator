from django.urls import path
from . import views

app_name = 'yt_transcription'

urlpatterns = [
    path('', views.index, name='index'),
]