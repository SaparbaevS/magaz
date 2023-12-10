from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView

from app.forms import ProductModelForm
from app.models import Magazin


class StartPage(TemplateView):
    template_name = 'app/index.html'


class AddProduct(CreateView):
    model = Magazin
    form_class = modelform_factory(Magazin, fields=['title', 'category', 'price', 'status'])
    template_name = 'app/add.html'
    success_url = reverse_lazy('administrator:start')


class ProductList(ListView):
    model = Magazin
    template_name = 'app/products.html'
    context_object_name = 'products'


class UpdateProduct(UpdateView):
    model = Magazin
    form_class = ProductModelForm
    template_name = 'app/update.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
    success_url = reverse_lazy('administrator:start')

