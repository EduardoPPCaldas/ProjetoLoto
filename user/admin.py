from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario
# Register your models here.

class CustomUserAdmin(BaseUserAdmin):
  list_display = ("email" , "nome" , "cpf")
  list_filter = ("nome" , "email")
  fieldsets = ((None, {"fields": ("email", "nome", "cpf", "password")}),)

  ordering = ("email",)
  

admin.site.register(Usuario, CustomUserAdmin)