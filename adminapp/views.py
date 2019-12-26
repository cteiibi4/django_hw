from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import Product, ProductCategory
from authapp.models import ShopUser
#from .forms import ProductAdminForm

class IsSuperUserView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ProductListView(IsSuperUserView, ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка'
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(IsSuperUserView, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = f'{title}. Админка'
        return context

class ProductCreateView(IsSuperUserView, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    #success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Создание нового продукта. Админка'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk':self.object.pk})

class ProductUpdateView(IsSuperUserView, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin_custom:products')

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk':self.kwargs.get('pk')})

class ProductDeleteView(IsSuperUserView, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin_custom:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = 'Удаление {}. Админка'.format(title)
        return context

class UserListView(IsSuperUserView, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    queryset = ShopUser.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка'
        return context

class UserDetailView(IsSuperUserView, DetailView):
    model = ShopUser
    template_name = 'adminapp/user.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super( UserDetailView, self).get_context_data(**kwargs)
        title = ShopUser.objects.get(pk=self.kwargs.get('pk')).username
        context['title'] = f'{title}. Админка'
        return context