from django.shortcuts import render, redirect
from django.core import serializers
import json
from music.models import Library

def library_page(request):
    if not request.user.is_authenticated:
        return redirect('music:landing')
    
    try:
        library = request.user.library
        songs = library.songs.all()
    except:
        songs = []
    
    # Serialize songs to JSON
    songs_data = []
    for song in songs:
        songs_data.append({
            'id': song.id,
            'title': song.title,
            'genre': song.genre,
            'mood': song.mood,
            'duration': song.duration or 0,
            'occasion': song.occasion,
            'voiceTone': song.voice_tone,
            'coverHue': getattr(song, 'cover_hue', 215)
        })
    
    songs_json = json.dumps(songs_data)
    
    return render(request, 'library.html', {
        'songs': songs,
        'songs_json': songs_json
    })