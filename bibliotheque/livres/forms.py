from django import forms
from django.shortcuts import redirect, render
from .models import Livre

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'date_publication']
        
        
        
