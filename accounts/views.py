from django.shortcuts import render, redirect
from .froms import signupForm, createPlaylistForm,createPlaylistLinkForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from main.models import playlistlink,playlist

Users=get_user_model()

def home(request, *args, **kwargs):
    user = request.user
    form = createPlaylistLinkForm(request.POST or None)
    form.fields['relatedPlaylist'].queryset = playlist.objects.filter(createdBy = user)
    if request.method == 'POST' and form.is_valid():

        form.save()
    context = {'form':form}
    return render(request, 'accounts/welcome.html', context)

def createPlaylist(request):
    form = createPlaylistForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        currentUser = request.user
        instance.createdBy = currentUser
        instance.save()
    context = {'form':form}
    return render(request, 'accounts/create_playlist.html', context)

def signup(request):
    form = signupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('accounts:login')
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        rawPassword = request.POST.get('password')
        user = authenticate(username=username, password=rawPassword)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
        else:
            print('Wrong Username or Pass')
    return render(request, 'accounts/login.html')

def userLogout(request):
    logout(request)
    return redirect('accounts:login')

