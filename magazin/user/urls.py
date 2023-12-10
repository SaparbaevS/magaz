from django.urls import path, include


from user.views import ProductList, StartPage, ProductDetail

app_name = 'users'

urlpatterns = [
    path('start/', StartPage.as_view(), name='start'),
    path('products/', ProductList.as_view(), name='products'),
    path('products/<slug:slug_param>/', ProductDetail.as_view(), name='detail')

]