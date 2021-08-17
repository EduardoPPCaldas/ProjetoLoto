from django.shortcuts import render
from .models import Resultados

# Create your views here.
def resultados(request):
  todos_resultados = Resultados.objects.order_by(
    "concurso"
  )

  context = {
    "todos_resultados" : todos_resultados
  }

  return render(request, "resultado.html", context)