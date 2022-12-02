from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class UserFormUpdate(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder':"Ex: Fred"
    }))
    class Meta:
        model = User
        fields = ('username',)
                  
class EnseignantForm(forms.ModelForm):
    nom = forms.CharField(label='Nom', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: Toto"
    }))
    post_nom = forms.CharField(label='Post-nom', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: Mukabaha"
    }))
    pre_nom = forms.CharField(label='Prénom', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: Frederick"
    }))
    genre = forms.CharField(label="Sexe", widget=forms.Select(choices=sexe_choice, attrs={
        'class': "form-control form-select custom-select",
    }))
    phone_number = forms.CharField(label='N° Phone', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: 970000000"
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: toto@gmail.com"
    }))
    is_admin = forms.BooleanField(label="Admin", required=False)
    
    class Meta:
        model = Enseignant
        fields = ('nom', 'post_nom', 'pre_nom', 'genre', 'phone_number', 'email', 'is_admin')
        
class SceanceForm(forms.ModelForm):
    promotion = forms.CharField(label='Promotion', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: G3-GEI-FSTA"
    }))
    cours = forms.CharField(label='Scéance', widget=forms.TextInput(attrs={
        'class': "form-control mb-3",
        'placeholder':"Ex: Base des données"
    }))
    
    class Meta:
        model = Sceance
        fields = ('promotion', 'cours')
        

class PasswwordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label="Ancien mot de passe", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':"Ex: Password",
        'type': 'password'
    }))
    new_password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':"Ex: new_password",
        'type': 'password'
    }))
    new_password2 = forms.CharField(label="Confirmation nouveau mot de passe", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder':"Ex: new_password",
        'type': 'password'
    }))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')