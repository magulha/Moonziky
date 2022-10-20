from django.contrib import admin
from django.contrib.auth.models import User
from .models import Playlist, Music
# Register your models here.
admin.site.register(Playlist)
admin.site.register(Music)