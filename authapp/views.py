from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from .forms import ShopUserRegisterForm
from .models import ShopUser

# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()

    context = {
        'form': register_form,
        'title': 'Регистрация',
        'submit_label': 'Зарегистрироваться'
    }
    return render(request, 'authapp/register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if request.POST.get('next'):
                return HttpResponseRedirect(request.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('main'))

    context = {'next': request.GET.get('next'),
               'title': 'Войти',
               }
    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

class EditView(UpdateView):
    model = ShopUser
    template_name = 'authapp/register.html'
    fields = 'username', 'email', 'avatar'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        context['submit_label'] = 'Применить'
        return context