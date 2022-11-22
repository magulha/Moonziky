from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),
    path('home', views.home, name='home'),
    path('playlist', views.createPlaylist, name='create_playlist'),
]
