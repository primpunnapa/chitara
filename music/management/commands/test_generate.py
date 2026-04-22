from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from music.strategies import get_generator_strategy
from music.models import Library
from music.services.song_service import SongGenerationContext

class Command(BaseCommand):
    help = "Test song generation using selected strategy"

    def add_arguments(self, parser):
        parser.add_argument('--strategy', type=str, default='mock')

    def handle(self, *args, **options):
        strategy_name = options['strategy']

        # 1. Get strategy
        strategy = get_generator_strategy(strategy_name)

        # 2. Create/get test user
        User = get_user_model()
        user, _ = User.objects.get_or_create(username="testuser")

        # 3. Create/get library
        library, _ = Library.objects.get_or_create(user=user)

        # 4. Prepare data (match your model fields!)
        data = {
            "title": "Test Song",
            "genre": "Classical",
            "mood": "Peaceful",
            "occasion": "Relaxation",
            "voice_tone": "Soft",
            "prompt": "Relaxing piano music",
            "customMode": False,
            "instrumental": True,
            "model": "V4_5ALL",
            "callBackUrl": "https://example.com/callback"
        }

        # 5. Use Context
        context = SongGenerationContext(strategy)
        song = context.generate_song(user, data)

        # 6. Output result
        self.stdout.write(self.style.SUCCESS(f"Song saved: {song.id}"))
        self.stdout.write(self.style.SUCCESS(f"Title: {song.title}"))
        self.stdout.write(self.style.SUCCESS(f"Audio URL: {song.audio_url}"))
        self.stdout.write(self.style.SUCCESS(f"Status: {song.generation_status}"))