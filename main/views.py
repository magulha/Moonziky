from xml.dom.minidom import Identified
from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Items

# Create your views here.
def index(response, name):
	ls = Playlist.objects.get(name=name)
	return render(response, "main/base.html", {})

def home(response):
	return render(response, "main/home.html", {})
