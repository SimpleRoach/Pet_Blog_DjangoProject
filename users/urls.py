from django.urls import path
from . import views as users_views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('reg/', users_views.regis, name='reg'),
    path('user/', users_views.singup, name='user')
]

