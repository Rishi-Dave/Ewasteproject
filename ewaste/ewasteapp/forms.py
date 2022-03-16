from django.forms import ModelForm
from .models import Item, CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class objectTypeForm(ModelForm):
    class Meta:
        model = Item
        fields = ['object_type']
class userSignInForm(UserCreationForm):
    """
    The default 

    """

    class Meta:
        model = CustomUser
        fields = ["email", "user_name", "first_name", "last_name", "address", "zip_code", "city"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
class userLogInForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["user_name", "password"] 
        


