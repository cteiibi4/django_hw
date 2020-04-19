from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, HttpResponse
from mainapp.models import Product
from .models import BasketSlot
from django.contrib.auth.decorators import login_required

@login_required
def add(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    old_basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    # print(product_pk)
    if old_basket_slot:
        old_basket_slot.quantity += 1
        old_basket_slot.save()
    else:
        new_basket_slot = BasketSlot(user=request.user, product=product)
        new_basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove(request, product_pk=None):
    # print(product_pk)
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket(request):
    title = 'Корзина'
    basket = BasketSlot.objects.filter(user=request.user).all()
    total_cost = 0
    total_quantity = 0
    for item in basket:
        total_cost += item.price
        total_quantity += item.quantity
    content = {
        'title': title,
        'basket': basket,
        'total_quantity': total_quantity,
        'total_cost': total_cost,
    }
    # print(basket)
    return render(request, 'mainapp/basket.html', content)

@login_required
def edit(request, pk):
    bs = get_object_or_404(BasketSlot, pk=pk)
    quantity = int(request.GET.get('quantity'))
    if quantity > 0:
        bs.quantity = quantity
        bs.save()
    else:
        bs.delete()
        bs.save()
    return HttpResponse('Ok')