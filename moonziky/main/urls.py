
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('follow/<int:pk>', views.followSystem, name="followSystem"),
    path('like/<int:pk>', views.likeSystem, name="likeSystem"),
]
