from django.db import models
from django.contrib.auth.models import (BaseUserManager , AbstractBaseUser, PermissionsMixin)
from phonenumber_field.modelfields import PhoneNumberField

class UsuarioManager(BaseUserManager):
  def create_user(self ,cpf , nome, telefone, email, password= None, **extra_fields):
    usuario = self.model(
      email = self.normalize_email(email),
      nome = nome,
      cpf = cpf,
      telefone = telefone,
      **extra_fields
    )
    usuario.is_active = True
    usuario.is_staff = False
    usuario.is_superuser = False

    if password:
      usuario.set_password(password)
    usuario.save()

    return usuario
  def create_superuser(self, email, cpf, telefone , nome , password):
    usuario = self.create_user(
      email = self.normalize_email(email),
      cpf = cpf,
      telefone = telefone,
      nome = nome,
      password = password,
    )

    usuario.is_active = True
    usuario.is_staff =  True
    usuario.is_superuser = True

    usuario.set_password(password)
    usuario.save()

    return usuario


class Usuario(AbstractBaseUser , PermissionsMixin):
  email = models.EmailField(
    verbose_name="E-mail do usuário",
    max_length=194,
    unique=True,
  )
  cpf = models.CharField(
    verbose_name="Cpf do usuário",
    max_length=11
  )
  nome = models.CharField(
    verbose_name="Nome completo do usuário",
    max_length=194
  )
  telefone = PhoneNumberField()
  is_active = models.BooleanField(
    verbose_name="Usuario está ativo",
    default=True,
  )

  is_staff = models.BooleanField(
    verbose_name="Usuário é da equipe de desenvolvimento",
    default=False,
  )
  is_superuser = models.BooleanField(
    verbose_name="Usuário é um superusuário",
    default=False
  )
  USERNAME_FIELD = "email"

  objects = UsuarioManager()

  REQUIRED_FIELDS = ["cpf", "nome", "telefone"]

  class Meta:
    verbose_name = "Usuário"
    verbose_name_plural = "Usuários"
    db_table = "usuario"

  def __str__(self):
      return self.email