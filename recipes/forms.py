from django.forms import modelform_factory
from django import forms

from recipes.models import Recipe

AddRecipeForm = modelform_factory(Recipe, exclude=[])

EditRecipeForm = modelform_factory(Recipe, exclude=[])

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)