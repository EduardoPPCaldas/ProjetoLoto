from django.db import models

# Create your models here.
class Resultados(models.Model):
  concurso = models.PositiveSmallIntegerField(
    verbose_name="Concurso"
  )
  data = models.DateField(
    verbose_name="Data"
  )

  primeiro_numero = models.PositiveSmallIntegerField(
    verbose_name="Primeiro Número"
  )
  segundo_numero = models.PositiveSmallIntegerField(
    verbose_name="Segundo Número"
  )
  terceiro_numero = models.PositiveSmallIntegerField(
    verbose_name="Terceiro Número"
  )
  quarto_numero = models.PositiveSmallIntegerField(
    verbose_name="Quarto Número"
  )
  quinto_numero = models.PositiveSmallIntegerField(
    verbose_name="Quinto Número"
  )
  sexto_numero = models.PositiveSmallIntegerField(
    verbose_name="Sexto Número"
  )
  setimo_numero = models.PositiveSmallIntegerField(
    verbose_name="Sétimo Número"
  )
  oitavo_numero = models.PositiveSmallIntegerField(
    verbose_name="Oitávo Número"
  )
  nono_numero = models.PositiveSmallIntegerField(
    verbose_name="Nono Número"
  )
  decimo_numero = models.PositiveSmallIntegerField(
    verbose_name="Decimo Número"
  )
  decimo_primeiro_numero = models.PositiveSmallIntegerField(
    verbose_name="Décimo Primeiro Número"
  )
  decimo_segundo_numero = models.PositiveSmallIntegerField(
    verbose_name="Décimo Segundo Número"
  )
  decimo_terceiro_numero = models.PositiveSmallIntegerField(
    verbose_name="Décimo Terceiro Número"
  )
  decimo_quarto_numero = models.PositiveSmallIntegerField(
    verbose_name="Décimo Quarto Número"
  )
  decimo_quinto_numero = models.PositiveSmallIntegerField(
    verbose_name="Décimo Quinto Número"
  )

  class Meta():
    verbose_name = "Resultado"
    verbose_name_plural = "Resultados"
    db_table = "resultado"

  def __str__(self):
    return self.concurso