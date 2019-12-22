from django.urls import path
from .views import add, remove, basket


app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='index'),
    path('add/<int:product_pk>', add, name='add'),
    path('remove/<int:product_pk>', remove, name='remove'),

]