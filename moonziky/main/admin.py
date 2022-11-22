from django.contrib import admin

from .models import playlist,playlistlink,favplyalist

admin.site.register(playlist)
admin.site.register(playlistlink)
admin.site.register(favplyalist)