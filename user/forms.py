from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

class CustomRegistrationForm(UserCreationForm):
  email = forms.EmailField(
    max_length=192,
    help_text="Email do usuário"
  )
  cpf = forms.CharField(
    max_length=11,
    help_text="CPF do usuário"
  )
  nome = forms.CharField(
    max_length=192,
    help_text="Nome completo do usuário"
  )
  telefone = PhoneNumberField()

  class Meta:
    model = Usuario
    fields = ("email" , "nome", "cpf", "telefone" , "password1", "password2")
    exclude = ["username",]