from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})

def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'Контакты'})

def catalog(request, pk=None):
    title = 'Каталог'
    products = Product.objects.all()
    category = ProductCategory.objects.all()
    if pk:
        products = products.filter(category=pk)
    content = {
        'title': title,
        'products': products,
        'categories': category,
        }
    return render(request, 'mainapp/catalog.html', content)

def product(request, pk=None):
    product = Product.objects.all()
    if pk:
        product = product.filter(id=pk).first()
        title = product.name
    content = {
        'title': title,
        'products': product,
    }
    return render(request, 'mainapp/product.html', content)