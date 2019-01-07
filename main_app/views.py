from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView, UpdateView
from main_app.models import *
from main_app.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.


class FlowerView(ListView):
    model = Flower


class OrderView(ListView):
    model = Order


class UserView(ListView):
    model = User



def static_main(request):
    return render(request, 'main.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(FormView):
    model = User
    template_name = 'registration/profile.html'
    form_class = UpdateUserForm                     # uh

    def get_initial(self):
        super(ProfileView, self).get_initial()
        model = User.objects.get(id=self.request.user.id)
        self.initial = {
            'username': model.username,
            'first_name': model.first_name,
            'last_name': model.last_name,
        }
        return self.initial

@method_decorator(login_required, name='dispatch')
class UpdateProfileView(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name']
    success_url = '/accounts/profile'

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

class IndexView(TemplateView):
    def get(self, *args, **kwargs):
        data = {
            'flowers': Flower.objects.all(),
            'front_page': True
        }
        return render(self.request, 'index.html', data)