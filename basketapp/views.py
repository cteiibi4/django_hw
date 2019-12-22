from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from mainapp.models import Product
from .models import BasketSlot

def add(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    old_basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if old_basket_slot:
        old_basket_slot.quantity += 1
        old_basket_slot.save()
    else:
        new_basket_slot = BasketSlot(user=request.user, product=product)
        new_basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def basket(request):
    title = 'Корзина'
    basket = BasketSlot.objects.filter(user=request.user).all()
    total_quantity = 0
    for item in basket:
        total_quantity += item.price
    content = {
        'title': title,
        'basket': basket,
        'total_quantity': total_quantity,
    }
    print(basket)
    return render(request, 'mainapp/basket.html', content)