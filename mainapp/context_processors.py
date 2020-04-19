from basketapp.models import BasketSlot

def basket(request):
   #print(f'context processor basket works')
   basket = []
   if request.user.is_authenticated:
       # basket = request.user.BasketSlot.select_related()
       basket = BasketSlot.objects.filter(user=request.user)
   return {
       'basket': basket,
   }