from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from fishshop import settings
from .models import ProductCategory, Product


def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})


def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'Контакты'})


@cache_page(3600)
def catalog(request, pk=None):
    title = 'Каталог'
    products = Product.objects.all()
    category = ProductCategory.objects.all()
    if pk is None:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {
            'title': title,
            'hot_product': hot_product,
            'categories': category
        }
        return render(request, 'mainapp/hot_product.html', context)
    if pk > 0:
        products = products.filter(category=pk)
    content = {
        'title': title,
        'products': products,
        'categories': category,
    }
    return render(request, 'mainapp/catalog.html', content)


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def product(request, pk):
    # product = Product.objects.all()
    if pk:
        product = get_product(pk)
        title = product.name
    content = {
        'title': title,
        'product': product,
    }
    return render(request, 'mainapp/product.html', content)


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)
