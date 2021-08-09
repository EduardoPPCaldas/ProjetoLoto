from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Usuario
# Register your models here.

admin.site.register(Usuario, auth_admin.UserAdmin)