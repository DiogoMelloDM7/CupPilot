from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já esta em uso. Por favor, escolha outro")
        return email
