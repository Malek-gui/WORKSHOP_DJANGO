from django import forms
from .models import Entreprise,User
from django.contrib.auth.forms import UserCreationForm


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = '__all__'



class RegistrationUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'telephone')