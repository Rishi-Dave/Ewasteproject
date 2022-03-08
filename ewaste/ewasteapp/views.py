from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from ewasteapp.forms import  objectTypeForm, userSignInForm
from .models import Item, CustomUser

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def home_page(request):
    return render(request, "index.html")
class ItemPickupView(CreateView):
    model = Item
    form_class = objectTypeForm
    template_name = 'pickup.html'
    success_url = 'pickup.html'

class UserView(CreateView):
    form_class = userSignInForm
    template_name = 'signup.html'
    success_url = 'login.html'

def pickup(request):
    return render(request, 'pickup.html',)

def postpickup(request):
    return render(request, 'postpickup.html',)

def user_login(request):
    if request.method == "POST":
       username = request.POST["username"] 
       pass1 = request.POST['pass1']

       user = authenticate(username = username, password = pass1)
       if user is not None:
           login(request, user)
           fname = user.first_name
           address = user.street_address
           return render(request, "index.html", {"fname":fname}, {"address":address})
       else:
            messages.error(request, "Bad Credentials")
            return redirect('login')
    return render(request, 'login.html')
"""""
def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = userSignInForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            form.save()
            return redirect('login')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = userSignInForm()

    return render(request, 'signup.html', {'form': form})
"""
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')
def driverlogin(request):
    return render(request, 'driverlogin.html')
    