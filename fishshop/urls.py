"""fishshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from mainapp.views import main, catalog, contacts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', catalog, name='catalog'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin_custom/', include('adminapp.urls', namespace='admin_custom')),
    path('admin/', admin.site.urls),
    path('auth/verify', include('social_django.urls', namespace='social')),
    path('order/', include('ordersapp.urls', namespace='order')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]