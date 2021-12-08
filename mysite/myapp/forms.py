from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Product, Customer


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'price', 'stock',)


class SignUpForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ('username', 'password1', 'password2',)