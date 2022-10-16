from django.urls import path
from . import views

# urlpatterns = [
# path("", views.index, name = "index"),
# path("v1/", views.v1, name = "view 1"),
# ]

urlpatterns = [
    path("playlist/<str:playlistName>", views.playlistPage, name="playlistPage"),
    path("", views.home, name="home")
]
