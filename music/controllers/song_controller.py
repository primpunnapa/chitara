from django.shortcuts import render, redirect
from music.strategies import get_generator_strategy
from music.services.song_service import SongGenerationContext

def generate_song_page(request):
    return render(request, 'generate_song.html')


def create_song(request):
    if request.method == 'POST':
        try:
            context = SongGenerationContext(get_generator_strategy())
            context.generate_song(request.user, request.POST)
            return redirect('library')
        except Exception as e:
            return render(request, 'generate_song.html', {
                'error': str(e)
            })

    return redirect('generate_song_page')