from django.shortcuts import render
from .models import Resultados
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def resultados(request):
  todos_resultados = Resultados.objects.order_by(
    "-concurso"
  )

  context = {
    "todos_resultados" : todos_resultados
  }

  return render(request, "resultado.html", context)