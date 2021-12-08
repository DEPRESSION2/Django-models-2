from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView

from .models import *
from .forms import ProductCreateForm, SignUpForm
# Create your views here.


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'index.html'
    login_url = 'login/'
    extra_context = {'create_form': ProductCreateForm()}
    paginate_by = 5

   
def index(request):
    return render(request, 'index.html')


class Login(LoginView):
    template_name = 'login.html'


class Register(CreateView):
    form_class = SignUpForm
    template_name = 'register.html'
    success_url = '/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    http_method_names = ['post']
    form_class = ProductCreateForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form=form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'index.html'
    success_url = '/'

