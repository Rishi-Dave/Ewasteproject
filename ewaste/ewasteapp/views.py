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
    success_url = '/login'
    def form_invalid(self,form):
            # Add action to invalid form phase
            messages.error(self.request, form.errors)
            return self.render_to_response(self.get_context_data(form=form))
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
           address = user.address
           return render(request, "index.html", {"fname":fname}, {"address":address})
       else:
            messages.error(request, "Bad Credentials")
            return redirect('login')
    return render(request, 'login.html')
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')
def driverlogin(request):
    return render(request, 'driverlogin.html')
    