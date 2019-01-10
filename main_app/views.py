import sys

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView, ListView, UpdateView
from main_app.models import *
from main_app.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django_ajax.decorators import ajax
from django.shortcuts import render, redirect

# Create your views here.

@ajax
def get_flower(request):
    if request.method != 'GET':
        return
    flower = Flower.objects.get(pk=request.GET['id'])
    return {'price': flower.price,
            'country': flower.country,
            'name': flower.flower_name,
            'color': flower.color,
            'img': flower.img}


@ajax
def edit_flower(request):
    if request.method == 'POST':
        if request.is_ajax():
            flower = Flower.objects.get(pk=request.POST['id'])
            if flower:
                if request.POST['flower_name']:
                    flower['flower_name'] = request.POST['flower_name']
                if request.POST['price']:
                    flower['price'] = request.POST['price']
                if request.POST['color']:
                    flower['color'] = request.POST['color']
                if request.POST['country']:
                    flower['country'] = request.POST['country']
                if request.POST['img']:
                    flower['img'] = request.POST['img']
                flower.save(commit=True)


@ajax
def set_flower_photo(request):
    if request.method == 'POST' and request.is_ajax():
        form = FlowerForms.SetFlowerPhotoForm(request)
        if form.is_valid():
            form.save(commit=True)


def add_flower(request):
    pass


class OrderOfFlower:
    def prepare_subjects(self, flower, request):
        from django.db.models import Count
        from django.db.models import Q
        orders = Order.objects.filter(Q(flower_order=flower))
        orders = orders.annotate(dcount=Count('id')).order_by('-flower')
        # пагинация
        from django.core.paginator import Paginator
        paginator = Paginator(orders, 10)
        return paginator.get_page(self.request.GET.get('page'))


class FlowerView(TemplateView, OrderOfFlower):
    def get(self, *args, **kwargs):
        data = {
            'flower': Flower.objects.get(pk=kwargs['id']),
            'add-form': FlowerForms.AddFlowerForm(),
            'form': FlowerForms.SetFlowerPhotoForm()  # TODO: what is this?
        }
        return render(self.request, 'main_app/flower_item.html', data)


class UpdateFlowerView(UpdateView):
    model = Flower
    fields = ['img']

    def get_object(self):
        return Flower.objects.get(id=self.kwargs['id'])

    def get_success_url(self):
        return reverse('flower', kwargs={'id': self.object.id})

# class FlowerView(TemplateView):
#     def get(self, *args, **kwargs):
#         data = {
#             'teacher': Flower.objects.filter(id=kwargs['id']).first(),
#         }
#         return render(self.request, 'flower_item.html', data)


# class OrderView(ListView):
#     model = Order


class UsersView(ListView):
    model = User


@login_required(login_url='accounts/login')
def static_main(request):
    return render(request, 'main.html')


@method_decorator(login_required, name='dispatch')
class ProfileView(FormView):
    model = User
    template_name = 'registration/profile.html'
    form_class = UserForms.UpdateUserForm

    def get_initial(self):
        super(ProfileView, self).get_initial()
        model = User.objects.get(pk=self.request.user.id)
        self.initial = {
            'first_name': model.first_name,
            'last_name': model.last_name,
            'avatar': model.avatar
        }
        return self.initial


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):  # is this really needed?
    model = User
    form_class = UserForms.CustomUserChangeForm

    # fields = ['username', 'first_name', 'last_name', 'avatar']
    success_url = '/accounts/profile'

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)


class IndexView(TemplateView):
    model = Flower

    def get(self, *args, **kwargs):
        data = {
            'flowers': Flower.objects.all(),
            # 'front_page': True
        }
        return render(self.request, 'index.html', data)


class OrdersView(FormView):
    model = Order
    template_name = 'main_app/order_list.html'  # TODO
    form_class = OrderForms.OrderForm
