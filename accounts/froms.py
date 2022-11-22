from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from main.models import playlistlink, playlist

from django.forms import ModelForm
Users=get_user_model()

class signupForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = Users
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(signupForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
class createPlaylistLinkForm(ModelForm):
	#playlist = forms.ModelChoiceField(queryset=playlist.objects.none())
	class Meta:
		model = playlistlink
		fields = '__all__'
	
class createPlaylistForm(ModelForm):
	class Meta:
		model = playlist
		fields = ['nameOfPlaylist']
		exclude = ['createdBy']