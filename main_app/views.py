from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView
from main_app.models import *
from main_app.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class FlowerView(ListView):
    model = Flower


class OrderView(ListView):
    model = Order


class UserView(ListView):
    model = User

# this is comment


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
            'avatar': model.avatar
        }
        return self.initial
