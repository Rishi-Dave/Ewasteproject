from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Item
User = get_user_model()
admin.site.register(User)
admin.site.register(Item)