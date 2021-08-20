from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from user.forms import CustomRegistrationForm

# Create your views here.
@login_required
def index(request):

  return render(request, "index.html")

def signup(request):
  form = CustomRegistrationForm()

  context = {
    "sign_up_form" : form
  }

  return render(request, "signup.html", context)