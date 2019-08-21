from .views import user_login, user_register
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import dashboard, logout_user


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path("login/", user_login, name='login'),
    path("register/", user_register, name='register'),
    path('logout/', logout_user, name='logout'),

]
