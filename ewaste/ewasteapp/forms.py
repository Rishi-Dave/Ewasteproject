from django.forms import ModelForm
from .models import Item
from django import forms
from django.contrib.auth.forms import UserCreationForm

class objectTypeForm(ModelForm):
    class Meta:
        model = Item
        fields = ['object_type']
class userSignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=200)
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    password = forms.CharField(label = 'Password', max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(label = 'Confirm Password', max_length=32, widget=forms.PasswordInput)
    street_address = forms.CharField(label='Street Address', max_length=100)
    zip_code = forms.CharField(label='Zip Code', max_length=10)
    city = forms.CharField(label='City', max_length=100)




