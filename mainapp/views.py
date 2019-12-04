from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/main.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def catalog(request):
    return render(request, 'mainapp/catalog.html')
