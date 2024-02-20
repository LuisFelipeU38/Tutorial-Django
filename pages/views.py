from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect 
from django.views.generic import TemplateView, ListView
from django.views import View 
from django import forms 
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Product

# Create your views here.

# def homePageView(request): # new 
    # return HttpResponse('Hello World!') # new

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 

        context.update({ 

            "title": "About us - Online Store", 

            "subtitle": "About us", 

            "description": "This is an about page ...", 

            "author": "Developed by: Luis Felipe", 

        }) 
    
        return context 
    
def contactPageView(request):
    context = {
        'email' : 'luisfelipeCR7@something.com',
        'address' : 'El salado, San Javier',
        'phone' : '3128252314'
    }

    return render(request,'pages/contact.html', context)

'''class Product: 
    products = [ 

        {"id":"1", "name":"TV", "description":"Best TV", "price": 140000}, 

        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 1500}, 

        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 200}, 

        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 300} 

    ] '''

class ProductIndexView(View): 
    template_name = 'products/index.html' 

    def get(self, request): 

        viewData = {} 

        viewData["title"] = "Products - Online Store" 

        viewData["subtitle"] =  "List of products" 

        viewData["products"] = Product.objects.all() 

        return render(request, self.template_name, viewData) 

class ProductShowView(View): 

    template_name = 'products/show.html' 

    def get(self, request, id):
        viewData = {}

        # Check if product id is valid
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError):
            # If the product id is not valid, redirect to the home page
            return HttpResponseRedirect(reverse('home'))
        
        viewData = {}
        product = get_object_or_404(Product, pk=product_id)
        viewData["title"] = product.name + " - Online Store"
        viewData["subtitle"] =  product.name + " - Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)
    
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'  # This will allow you to loop through 'products' in your template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Products - Online Store'
        context['subtitle'] = 'List of products'
        return context

 

class ProductForm(forms.Form): 

    name = forms.CharField(required=True) 

    price = forms.FloatField(required=True)

    def correct_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:

            raise forms.ValidationError("Price error")

        return price

class ProductCreateView(View): 

    template_name = 'products/create.html' 

    def get(self, request): 

        form = ProductForm() 

        viewData = {} 

        viewData["title"] = "Create product" 

        viewData["form"] = form 

        return render(request, self.template_name, viewData) 

    def post(self, request): 

        form = ProductForm(request.POST) 

        if form.is_valid(): 
            return render(request, 'products/created_product.html')  

        else: 
            viewData = {} 

            viewData["title"] = "Create product" 

            viewData["form"] = form 

            return render(request, self.template_name, viewData)
    