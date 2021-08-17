from django.shortcuts import render

# Create your views here.
def resultados(request):
  return render(request, "resultado.html")