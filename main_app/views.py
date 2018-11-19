from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView
from main_app.models import *

# Create your views here.


class FlowerView(ListView):
    model = Flower

class OrderView(ListView):
    model = Order

class UserView(ListView):
    model = User

def static_main(request):
    return render(request, 'main.html')
