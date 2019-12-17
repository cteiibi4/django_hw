from django.shortcuts import render
from .models import ProductCategory, Product

def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})

def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'Контакты'})

def catalog(request):
    title = Product.objects.all()[:3]

    products = Product.objects.all()[:3]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/catalog.html', content)