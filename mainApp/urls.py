from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('profile', views.profile),
    path('addbook', views.add_book),
    path('logout', views.logout),
]