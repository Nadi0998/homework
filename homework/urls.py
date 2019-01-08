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
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    # path(r'accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/login', name='login'),
    path('accounts/logout', name='logout'),
    path('accounts/profile/', ProfileView.as_view(), name='user_profile'),
    path('accounts/profile/update/', UpdateProfileView.as_view(), name='update_user_profile'),
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserRegistrationForm), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('flowers/', FlowerView.as_view()),
    path('', static_main, name='main'),
    path('users/', UserView.as_view()),
    path('orders/', OrderView.as_view()),
    path(r'index/', IndexView.as_view(), name='index'),
    path(r'flower/<int:id>', FlowerView.as_view(), name='department')
]
