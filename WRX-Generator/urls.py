from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsletter_app.urls')),
    path('subscribe/', include('newsletter_app.urls', namespace='newsletter_app')),
    path('password_generator/', include('password_generator.urls', namespace='password_generator')),
    path('qrcode_generator/', include('qrcode_generator.urls', namespace='qrcode_generator')),
    path('shortener/', include('shortener.urls', namespace='shortener')),
    path('transcribe/', include('yt_transcription.urls', namespace='yt_transcription')),
]

