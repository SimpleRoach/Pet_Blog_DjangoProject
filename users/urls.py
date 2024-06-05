from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg/', views.regis, name='reg'),
    path('user/', views.singup, name='user')
]

# path('exit/', auth_views.LogoutView.as_view('users/exit.html'), name='exit')
