from django.urls import path
from mainapp.views import catalog

app_name = 'mainapp'

urlpatterns = [
    path('', catalog, name='index'),
    path('category/<int:pk>', catalog, name='category'),
]