from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from app.models import Magazin


class StartPage(TemplateView):
    template_name = 'users/start.html'


class ProductList(ListView):
    model = Magazin
    template_name = 'users/product_list.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    template_name = 'users/detail.html'
    model = Magazin
    slug_field = 'slug'
    slug_url_kwarg = 'slug_param'
