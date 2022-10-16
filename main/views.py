from xml.dom.minidom import Identified
from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Items

# Create your views here.
def playlistPage(response, playlistName):
	playlist = Playlist.objects.get(name=playlistName)
	return render(response, "main/playlist.html", {"playlistName": playlist.name})

def home(response):
	return render(response, "main/home.html", {})
