"""ewaste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ewasteapp import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('pickup/', views.PickupView.as_view(), name = 'pickup'),
    path('postpickup/', views.postpickup, name = 'postpickup'),
    path('login/', views.user_login, name = 'login'),
    path('signup/', views.sign_up, name = 'signup'),
    path('driversignup/', views.driver_sign_up, name = 'driversignup'),
    path('signout/', views.signout, name = 'signout'),
    path('admin/', admin.site.urls),
    path('driverlogin/', views.driverlogin, name = 'driverlogin'),
    path('driverview/', views.pickup_list, name = 'driverview')
    
]
urlpatterns += staticfiles_urlpatterns()
