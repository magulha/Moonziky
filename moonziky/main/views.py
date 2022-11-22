from django.shortcuts import render
from .models import playlist,favplyalist
from accounts.models import UserFollowing
from django.http import HttpResponse

def dashboard(request):
    allPlaylists = playlist.objects.all()
    context = {'Lista de Playlists': allPlaylists}
    return render(request, 'main/dashboard.html', context)

def followSystem(request, pk):
    followCreator = playlist.objects.get(id = pk)
    if request.method == "POST":
        if followCreator.createdBy == request.user:
            #print(followCreator.createdBy)
            #print(request.user)
            return HttpResponse("Você não pode se seguir")
        elif UserFollowing.objects.filter(user_id = followCreator.createdBy, following_user_id = request.user).exists():
            return HttpResponse("Você já segue este usuário")
        else:
            instance = UserFollowing(user_id = followCreator.createdBy, following_user_id = request.user)
            instance.save()
    context = {'Criador': followCreator.createdBy.username}
    return render(request, 'main/followPage.html', context)

def likeSystem(request, pk):
    getPlaylist = playlist.objects.get(id = pk)
    if request.method == 'POST':
        if favplyalist.objects.filter(likedPlaylist = getPlaylist, likedBy = request.user).exists():
            return HttpResponse('Você já curtiu essa playlist')
        else:
            instance = favplyalist(likedPlaylist = getPlaylist, likedBy = request.user)
            instance.save()
    context = {'Nome da playlist': getPlaylist}
    return render(request, 'main/likePage.html', context)
