"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from main_app.views import *
from main_app.forms.UserForms import CustomUserRegistrationForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path(r'^accounts/', include('django.contrib.auth.urls')),
    path(r'^accounts/register/',
         RegistrationView.as_view(form_class=CustomUserRegistrationForm),
         name='django_registration_register'),

    path(r'^accounts/', include('django_registration.backends.one_step.urls')),
    path(r'^accounts/profile/', ProfileView.as_view(), name='user_profile'),
    path(r'^accounts/profile/edit/', EditProfileView.as_view(), name='edit_user_profile'),
    path(r'^admin/', admin.site.urls),

    path(r'^users/', UsersView.as_view(), name='users'),
    path(r'^orders/', OrdersView.as_view(), name='orders'),
    path(r'flowers/', IndexView.as_view(), name='flowers'),
    path(r'flower/<int:id>', FlowerView.as_view(), name='flower'),
    path(r'flower/set_photo/<int:id>', UpdateFlowerView.as_view(), name='set_flower_photo'),
    path(r'^flower/edit$', edit_flower, name='edit_flower'),
    path(r'^flower/add$', add_flower, name='add_flower'),
    path(r'^flower/get$', get_flower),

    path('', static_main, name='main'),
]
