from django.db import models
from django.conf import settings

class Library(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Library"
    
    def add_song(self, song):
        self.song.add(song)
        self.save()
    
    def remove_song(self, song):
        self.song.remove(song)
        self.save()
    