from music.strategies import get_generator_strategy
from music.models import Song

class SongGenerationContext:

    def __init__(self, strategy):
        self._strategy = strategy

    def generate_song(self, user, data):
        result = self._strategy.generate(data)

        song = Song.objects.create(
            user=user,
            library=user.library,
            title=data['title'],
            audio_url=result.get("audio_url"),
            task_id=result.get("task_id"),
            genre=data['genre'],
            mood=data['mood'],
            occasion=data['occasion'],
            voice_tone=data['voice_tone'],
            description=data['description'],
            duration=result.get("duration"),
            generation_status=result.get("status")
        )

        return song