from django.urls import path

from .views import (ProductListView, Login, Register, Logout, ProductUpdateView, ProductCreateView)

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
   