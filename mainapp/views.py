from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/main.html', context={'title': 'Главная'})

def contacts(request):
    return render(request, 'mainapp/contacts.html', context={'title': 'Контакты'})

def catalog(request):
    context_catalog = {'title': 'Каталог', 'products': [{'link':'catalog/ramirezi.html', 'image' :'/static/img/ramirezi.jpg/', 'name' :'Микрогеофагус Рамиреса'},
                                                        {'link':'catalog/ramirezi_blue.html', 'image' :'/static/img/ramirezi_blue.jpg/', 'name' :'Микрогеофагус Рамиреса Electric Blue'},
                                                        {'link':'catalog/ramirezi_gold.html', 'image' :'/static/img/ramirezi_gold.jpg/', 'name' :'Микрогеофагус Рамиреса Gold'}]}
    return render(request, 'mainapp/catalog.html', context_catalog)

