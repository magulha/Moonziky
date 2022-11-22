from django.db import models
from django.contrib.auth import get_user_model
Users=get_user_model()


class playlist(models.Model):
    createdBy = models.ForeignKey(Users, on_delete=models.PROTECT)
    nameOfPlaylist = models.CharField(max_length=30)
    def __str__(self):
        return self.nameOfPlaylist

class playlistlink(models.Model):
    relatedPlaylist = models.ForeignKey('playlist', on_delete=models.PROTECT)
    linkOfPlaylist = models.URLField()
    def __str__(self):
        return self.linkOfPlaylist

class favplyalist(models.Model):
    likedPlaylist = models.ForeignKey('playlist', on_delete=models.CASCADE)
    likedBy = models.ForeignKey(Users, on_delete=models.PROTECT)