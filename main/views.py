from xml.dom.minidom import Identified
from django.shortcuts import render
from django.http import HttpResponse
from .models import Playlist, Music
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def playlistPage(response, playlistName):
	playlist = Playlist.objects.get(name=playlistName)
	return render(response, "main/playlist.html", {"playlistName": playlist.name})

def home(response):
	return render(response, "main/home.html", {})

def index(request):
    """View function for home page of site."""
	if request.user.is_authenticated:
		return HttpResponseRedirect("/home/")
	else:
		return render(request, "index.html")
    
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

def createplaylist_view(request):
	songs=song.objects
	if request.method == 'POST':
		playlist=Playlist()
		playlist=name=request.POST['nomedaplaylist']
		playlist.save()
		print(playlist.name)
		playlist.songs.add(*songs)
		return render(request, 'addsongs.html', {'songs':songs})
	else:
		return render(request, 'createplaylist.html',{'songs':songs})

def addsongs_view(request,pk):
	songs=Song.objects.all()
	playlist=Playlist.objects
	if request.method == 'POST':
		item=Song.objects.get(id=pk)
		playlist.song=item
		playlist.objects.update(song=item)
		return render(request, 'addsongs.html', {'songs':songs})
		return render(request, 'addsongs.html', {'songs':songs})

@require_POST
def cadastrar_usuario(request):
	try:
		usuario_aux = User.objects.get(email=request.POST['campo-email'])

		if usuario_aux:
			return render(request, 'index.html', {'msg': 'Erro! Ja existe um usuario com o mesmo email'})

	except User.DoesNotExist:
		Cadastrar usuário

	nome_usuario = request.POST['uname']
	email = request.POST['email']
	senha = request.POST['password']

	newUser = User.objects.create_user(username=nome_usuario, email=email, password=senha)
	newUser.save()

@require_POST
def entrar(request):
	usuario_aux = User.objects.get(email=require.POST['email'])
	usuario = authenticate(username=usuario_aux.username,
							password=request.POST["senha"])
	if usuario is not None:
		login(request, usuario)
		return HttpResponseRedirect('/home/')

	return HttpResponseRedirect('/')

@login_required
def sair(request):
	logout(request)
	return HttpResponseRedirect('/')

