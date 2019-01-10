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
from homework.views import login_redirect
from main_app.forms.UserForms import CustomUserRegistrationForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    # path(r'', login_redirect, name='login_redirect'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',
         RegistrationView.as_view(form_class=CustomUserRegistrationForm,
                                  template_name='registration/register.html'),
         name='django_registration_register'),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='user_profile'),
    path('accounts/profile/edit/', EditProfileView.as_view(), name='edit_user_profile'),
    path('admin/', admin.site.urls),

    path('users/', UsersView.as_view(), name='users'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('index/', IndexView.as_view(), name='index'),  # TODO: is this required?
    path('flowers/', FlowerView.as_view(), name='flowers'),
    path(r'flower/<int:id>', FlowerView.as_view()),

    path('', static_main, name='main'),
]
