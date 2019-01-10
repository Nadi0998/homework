from django.shortcuts import render
from django.views.generic import FormView, ListView, UpdateView
from main_app.models import *
from main_app.forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

# Create your views here.



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
        flower = kwargs['id']
        data = {
            'flower': Flower.objects.get(id=flower),
            'add-form': FlowerForms.AddFlowerForm(),
            'form': FlowerForms.SetFlowerPhotoForm()  # TODO: what is this?
        }
        return render(self.request, 'main_app/flower_list.html', data)

# class FlowerView(TemplateView):
#     def get(self, *args, **kwargs):
#         data = {
#             'teacher': Flower.objects.filter(id=kwargs['id']).first(),
#         }
#         return render(self.request, 'flower_list.html', data)


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
        model = User.objects.get(id=self.request.user.id)
        self.initial = {
            'username': model.username,
            'first_name': model.first_name,
            'last_name': model.last_name,
            'avatar': model.avatar
        }
        return self.initial


@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):  # is this really needed?
    model = User
    form_class = UserForms.CustomUserChangeForm
    fields = ['username', 'first_name', 'last_name', 'avatar']
    success_url = '/accounts/profile'

    # def get_object(self):
    #     return User.objects.get(id=self.request.user.id)


class IndexView(TemplateView):
    model = Flower

    def get(self, *args, **kwargs):
        data = {
            'flowers': Flower.objects.all(),
            'front_page': True
        }
        return render(self.request, 'index.html', data)


class OrdersView(FormView):
    model = Order
    template_name = 'main_app/order_list.html'  # TODO
    form_class = OrderForms.OrderForm
