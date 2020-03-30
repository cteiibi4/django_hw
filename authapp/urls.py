from django.urls import path, re_path
import authapp.views as authapp
app_name = 'authapp'

urlpatterns = [
    path('register/', authapp.register, name='register'),
    path('login/', authapp.login, name='login'),
    path('edit/<int:pk>', authapp.EditView.as_view(), name='edit'),
    path('logout/', authapp.logout, name='logout'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]