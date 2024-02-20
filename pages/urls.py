from django.urls import path 
from .views import HomePageView, AboutPageView, contactPageView, ProductIndexView, ProductCreateView, ProductShowView, ProductCreateView, ProductCreated

urlpatterns = [ 
    path('', HomePageView.as_view(), name='home') ,
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contactPageView, name='contact'),
    path('products/', ProductIndexView.as_view(), name='index'), 
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('product_created/', ProductCreated, name='product-created'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
] 


