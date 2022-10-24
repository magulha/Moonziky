from xml.dom.minidom import Identified
from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Music
from django.views import generic

# Create your views here.
def playlistPage(response, playlistName):
	playlist = Playlist.objects.get(name=playlistName)
	return render(response, "main/playlist.html", {"playlistName": playlist.name})

def home(response):
	return render(response, "main/home.html", {})

def index(request):
    """View function for home page of site."""
    
    numPlaylist = Playlist.objects.all().count()
    numMusic = Music.objects.count()

    context = { #context são as variáveis de sistema que serão usadas na tela, ou seja, o contexto da aplicação
        'numPlaylist': numPlaylist,
        'numMusic': numMusic,
    }

	# Render the HTML template index.html with the data in the context variable
    return render(request, 'main/index.html', context=context)

class PlaylistListView(generic.ListView):
	model = Playlist
	templateName = 'main/playlist_list.html'

	def get_queryset(self):
		return Playlist.objects.all()

	def get_context_data(self, **kwargs):
		context = super(PlaylistListView, self).get_context_data(**kwargs)
		context['some_data'] = 'This is just some data'
		return context

class PlaylistDetailView(generic.DetailView):
	model = Playlist

