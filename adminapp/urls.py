from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.my_admin, name='my_admin'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('users/read/', adminapp.UserListView.as_view(), name='users'),
    path('users/read/<int:pk>/', adminapp.UserDetailView.as_view(), name='user_read'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),
    path('categorys/read/', adminapp.CategoryListView.as_view(), name='categorys'),
    path('categorys/read/<int:pk>/', adminapp.CategoryDetailView.as_view(), name='category_read'),
    path('categorys/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categorys/update/<int:pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categorys/delete/<int:pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),
]