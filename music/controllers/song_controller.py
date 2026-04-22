from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from music.strategies import get_generator_strategy
from music.services.song_service import SongGenerationContext
from music.models.song import Song

def generate_song_page(request):
    return render(request, 'generate_song.html')

@login_required
@require_http_methods(["POST"])
def create_song(request):
    try:
        context = SongGenerationContext(get_generator_strategy())
        song = context.generate_song(request.user, request.POST)
        return JsonResponse({
            'success': True,
            'song_id': song.id,
            'message': 'Song created successfully!'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

@login_required
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id, user=request.user)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'rename':
            new_title = request.POST.get('title', '').strip()
            if new_title:
                song.rename(new_title)
                return redirect('music:song_detail', song_id=song.id)
        
        elif action == 'delete':
            song.delete()
            return redirect('music:library')
    
    return render(request, 'song_detail.html', {
        'song': song,
        'created_date': song.created_at.strftime('%B %d, %Y')
    })