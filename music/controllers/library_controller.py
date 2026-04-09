from django.shortcuts import render
from music.models import Library

def library_page(request):
    library = request.user.library
    songs = library.songs.all()
    return render(request, 'library.html', {'songs': songs})