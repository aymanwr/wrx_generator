from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()
    language_sign = forms.ChoiceField(choices=[('EN', 'English'), ('AR', 'Arabic'), ('FR', 'French')])

class YoutubeForm(forms.Form):
    youtube_url = forms.URLField()
    language_sign = forms.ChoiceField(choices=[('EN', 'English'), ('AR', 'Arabic'), ('FR', 'French')])
