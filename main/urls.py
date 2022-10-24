from django.urls import path
from . import views

# urlpatterns = [
# path("", views.index, name = "index"),
# path("v1/", views.v1, name = "view 1"),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    # path("playlist/<str:playlistName>", views.playlistPage, name="playlistPage"),
    path('playlist/', views.PlaylistListView.as_view(), name='playlist'),
    path('playlist/<int:pk>', views.PlaylistDetailView.as_view(), name='playlist-detail'), # 1º A URL, 2º A View, 3º O nome da View
    #path('musics/<int:pk>', views.MusicDetailView.as_view(), name='musics-detail'),
    path('createplaylist/',views.createplaylist_view,name='createplaylist'),
    path('createplaylist/<int:pk>',views.addsongs_view,name='addsongs')
]
