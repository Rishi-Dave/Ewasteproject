from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import generic

from ewasteapp.forms import MyModelForm
from .models import Item
# Create your views here.
def home_page(request):
    return render(request, "index.html")
class ItemPickupView(generic.ListView):
    model = Item
    form_class = MyModelForm
    template_name = 'pickup.html'
    success_url = 'success.html'
def pickup(request):
    return render(request, 'pickup.html',)

def postpickup(request):
    return render(request, 'postpickup.html',)

def login(request):
    return render(request, 'login.html',)

def signup(request):
    return render(request, 'signup.html',)

def driverlogin(request):
    return render(request, 'driverlogin.html')