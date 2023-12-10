from django.urls import path, include

from app.views import StartPage, AddProduct, ProductList, UpdateProduct

app_name = 'administrator'

urlpatterns = [
    path('', StartPage.as_view(), name="start"),
    path('administrator/add/', AddProduct.as_view(), name='add'),
    path('administrator/products/', ProductList.as_view(), name='products'),
    path('administrator/products/<slug:slug_param>/update', UpdateProduct.as_view(), name='update')

]