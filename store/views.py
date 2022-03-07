from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Product, Category

# Create your views here.

# def categories(request): to add a default return function to all views 
#     return {
#         'categories': Category.objects.all()
#     }

def all_products(request):

    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'store/home.html', {'products': products, 'categories': categories})


def one_product(request, id):

    product = Product.objects.get(id = id)
    categories = Category.objects.all()
    return render(request, 'store/details.html', {'product': product, 'categories': categories})


def category_product(request, name):

    category = get_object_or_404(Category, name=name)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'store/category.html', {'category': category,'products': products, 'categories': categories})