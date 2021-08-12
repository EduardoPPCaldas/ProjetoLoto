from django.shortcuts import render
from .models import Usuario

# Create your views here.
def index(request):
  # context = {
  #   "nome" : ""
  # }

  return render(request, "index.html")