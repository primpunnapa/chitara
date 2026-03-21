from django.contrib import admin
from .models import User, Library, Song

admin.site.register(User)
admin.site.register(Library)
admin.site.register(Song)