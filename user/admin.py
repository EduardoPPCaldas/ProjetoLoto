from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario

from .forms import CustomRegistrationForm

class CustomUserAdmin(BaseUserAdmin):
  add_form = CustomRegistrationForm
  model = Usuario
  
  list_display = ("email" , "nome" , "cpf", "telefone")
  list_filter = ("nome" , "email")
  fieldsets = (
    (None, {"fields": ("email", "nome", "cpf","telefone", "password")}),
    ("User Type", {"fields" : ("is_superuser",)})
  )
  add_fieldsets = (
    (None, {"fields":("email", "nome", "cpf", "telefone", "password1", "password2")}),
  )
  exclude = ("username",)

  ordering = ("email",)
  

admin.site.register(Usuario, CustomUserAdmin)


