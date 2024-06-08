from django.urls import path
from . import views as users_views

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', users_views.user_signup, name='sig'),
    path('login/', users_views.user_login, name='log'),
    path('logout/', users_views.user_logout, name='logout'),
    path('profile/', users_views.user_profile, name='prof'),
]

