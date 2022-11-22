from django.shortcuts import render
from .models import playlist,favplyalist
from accounts.models import UserFollowing
from django.http import HttpResponse

def dashboard(request):
    allPlaylists = playlist.objects.all()
    context = {'listOfPlaylists': allPlaylists}
    return render(request, 'main/dashboard.html', context)

def followSystem(request, pk):
    followCreator = playlist.objects.get(id = pk)
    if request.method == "POST":
        if followCreator.createdBy == request.user:
            #print(followCreator.createdBy)
            #print(request.user)
            return HttpResponse("You Cannot Follow Yourself")
        elif UserFollowing.objects.filter(user_id = followCreator.createdBy, following_user_id = request.user).exists():
            return HttpResponse("You Are Already Following This User")
        else:
            instance = UserFollowing(user_id = followCreator.createdBy, following_user_id = request.user)
            instance.save()
    context = {'Creator': followCreator.createdBy.username}
    return render(request, 'main/followPage.html', context)

def likeSystem(request, pk):
    getPlaylist = playlist.objects.get(id = pk)
    if request.method == 'POST':
        if favplyalist.objects.filter(likedPlaylist = getPlaylist, likedBy = request.user).exists():
            return HttpResponse('You have already Liked this Playlist')
        else:
            instance = favplyalist(likedPlaylist = getPlaylist, likedBy = request.user)
            instance.save()
    context = {'playlistName': getPlaylist}
    return render(request, 'main/likePage.html', context)