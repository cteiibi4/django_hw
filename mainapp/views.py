from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})

def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'Контакты'})

def catalog(request, pk=None):
    title = 'Каталог'
    #title = Product.objects.all()[:2]

    products = Product.objects.all()[:3]
    category = ProductCategory.objects.all()
    content = {
        'title': title,
        'products': products,
        'categories': category,
        }
    return render(request, 'mainapp/catalog.html', content)