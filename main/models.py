from django.db import models
from django.urls import reverse


# Create your models here.
class Playlist(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('playlist-detail', args=[str(self.id)])
    
class Music(models.Model):
    playlist=models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='musics')
    name=models.CharField(max_length=300)
    complete=models.BooleanField()

    def __str__(self):
        return self.name