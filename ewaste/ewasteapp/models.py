from contextlib import nullcontext
from django.db import models
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.conf import settings
#user manager
class CustomUserManager(BaseUserManager):
	def create_superuser(self, email, user_name ,password, **other_fields):

		other_fields.setdefault('is_staff', True)
		other_fields.setdefault('is_superuser', True)
		other_fields.setdefault('is_active', True)

		if other_fields.get('is_staff') is not True:
			raise ValueError(
				'Superuser must be assigned to is_staff=True.')
		if other_fields.get('is_superuser') is not True:
			raise ValueError(
				'Superuser must be assigned to is_superuser=True.')
		
		user = self.create_user(email, user_name, "rishi", "dave", password, "none", "non","none" )
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_active = True
		user.save()
		return user
	def create_user(self, email, user_name, first_name, last_name, password, address, zip_code, city):
		if not email:
			raise ValueError(_('You must provide an email address'))

		email = self.normalize_email(email)
		user = self.model(email=email, user_name=user_name, first_name=first_name, last_name = last_name, address = address, zip_code = zip_code, city = city)
		user.set_password(password)
		user.is_active = True
		user.save()
		return user
class CustomUser(AbstractUser, PermissionsMixin):
	username = None
	email = models.EmailField(_('email address'))
	user_name = models.CharField(max_length=150, blank=True, unique = True)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	start_date = models.DateTimeField(default=timezone.now)
	address = models.CharField(max_length=300) 
	is_active = models.BooleanField(default=True)
	zip_code = models.CharField(max_length=12)
	city = models.CharField(max_length=1024)
	objects = CustomUserManager()
	is_driver = models.BooleanField(default=False)
	USERNAME_FIELD = 'user_name'
	REQUIRED_FIELDS = ['email']

class ItemList(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	item_list = []
	is_delivered = models.BooleanField(default=False)

class Item(models.Model):
	itemlist = models.ForeignKey(ItemList, on_delete=models.CASCADE)
	OBJECT_TYPE_CHOICES = (
		("battery", "battery"),
		("none" , "none"),
		("monitor" , "monitor"), #think of more later
	)
	object_type = models.CharField(
		max_length = 20,
		choices = OBJECT_TYPE_CHOICES,
		default = "none"
	)
	
	