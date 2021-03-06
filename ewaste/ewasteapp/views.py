from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.views.generic.edit import CreateView
from ewasteapp.forms import  DriverSignInForm, pickupForm, userLogInForm, userSignInForm
from .models import CustomUser, Item
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import formset_factory
import datetime
# Create your views here.
def home_page(request):
    return render(request, "index.html")

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = userSignInForm()
        if request.method == 'POST':
            form = userSignInForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('user_name')
                email = form.cleaned_data.get('email')
                '''''
                htmly = get_template('Email.html')
                d = { 'username': username }
                subject, from_email, to = 'welcome', 'electronicsrecylingservice@gmail.com', email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send() 
                '''  
                messages.success(request, 'Account was created for ' + username)
                
                return redirect('login')
            else:
                # Add action to invalid form phase
                messages.error(request, form.errors)
        context = {"form" : form}
        return render(request, 'signup.html', context)

def pickup(request):
    if not request.user.is_authenticated:
            messages.error(request, "Please Log in before requesting a pickup")
            return redirect('home')
    else:
        if request.method == 'POST':
            PickupFormSet = formset_factory(pickupForm, extra = 3)
            formset = PickupFormSet(request.POST)
            if formset.is_valid():
                request.user.pickup_requested = True
                request.user.save()
                for form in formset:
                    obj = form.save(commit = False)
                    obj.user = request.user
                    obj.save()
                return redirect('home')
        else:
            PickupFormSet = formset_factory(pickupForm, extra = 3)
            formset = PickupFormSet(None)
        context = {"formset" : formset}
        return render(request, 'pickup.html', context)


def postpickup(request):
    return render(request, 'postpickup.html')

def user_login(request):
    if request.method == 'POST':
        form = userLogInForm(request, data = request.POST)
        if form.is_valid(): 
            
            user = form.get_user()
            if user is not None:
                login(request, user)
                messages.success(request, "Logged In Successfully!!")
                return redirect('login')
            else:
                messages.error(request, "Bad Credentials")
                return redirect('login')
    else:
        form = userLogInForm(request)
    context = {"form" : form}
    return render(request, 'login.html', context)
def driver_sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = DriverSignInForm()
        if request.method == 'POST':
            form = DriverSignInForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('user_name')
                email = form.cleaned_data.get('email')
                '''''
                htmly = get_template('Email.html')
                d = { 'username': username }
                subject, from_email, to = 'welcome', 'electronicsrecylingservice@gmail.com', email
                html_content = htmly.render(d)
                msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()   
                '''
                messages.success(request, 'Account was created for ' + username)
                
                return redirect('login')
            else:
                # Add action to invalid form phase
                messages.error(request, form.errors)
        context = {"form" : form}
        return render(request, 'signup.html', context)
def driverview(request):
    l1 = CustomUser.objects.filter(pickup_requested = True)
    user_list = l1.filter(zip_code = 94555)
    context = {
    'user_list': user_list
    }  
    return render(request, 'driver_view.html', context)
def delete(request):
    items = Item.objects.filter(user=request.user)
    request.user.pickup_requested = False
    request.user.save()
    for instance in items:
        instance.delete()
    return redirect('pickup')
def delivered(request, obj_id):
    user = CustomUser.objects.get(pk=obj_id)
    user.pickup_requested = False
    user.save()
    items = Item.objects.filter(user=user)
    for instance in items:
        instance.picked_up_date = datetime.datetime.now()
        instance.save()
    return redirect('driverview')
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')

def driverlogin(request):
    return render(request, 'driverlogin.html')
    