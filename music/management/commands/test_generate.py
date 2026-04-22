from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from music.strategies import get_generator_strategy
from music.models import Library, Song
from music.services.song_service import SongGenerationContext


class Command(BaseCommand):
    help = "Test song generation OR recover song using task_id"

    def add_arguments(self, parser):
        parser.add_argument('--strategy', type=str, default='mock')
        parser.add_argument('--task_id', type=str, help='Existing Suno task ID')

    def handle(self, *args, **options):
        strategy_name = options['strategy']
        task_id = options.get('task_id')

        # 1. Get strategy
        strategy = get_generator_strategy(strategy_name)

        # 2. Create/get test user
        User = get_user_model()
        user, _ = User.objects.get_or_create(username="testuser")

        # 3. Create/get library
        library, _ = Library.objects.get_or_create(user=user)

        # CASE 1: Recover existing song (NO CREDIT USED)
        if task_id:
            self.stdout.write(f"Checking existing task: {task_id}")

            result = strategy.check_status(task_id)

            if result and result.get("status") == "SUCCESS":
                song = Song.objects.create(
                    user=user,
                    library=library,
                    title=result.get("title", "Recovered Song"),
                    audio_url=result.get("audio_url") or "",
                    task_id=task_id,
                    genre="CLASSICAL",
                    mood="SAD",
                    occasion="RELAXATION",
                    voice_tone="FEMALE",
                    generation_status="SUCCESS",
                    duration=result.get("duration")
                )

                self.stdout.write(self.style.SUCCESS(f"Recovered Song saved: {song.id}"))
                self.stdout.write(self.style.SUCCESS(f"Audio URL: {song.audio_url}"))

            else:
                self.stdout.write(self.style.ERROR("Task not ready or failed"))

            return  # stop here

        # CASE 2: Mock
        if strategy_name == "mock":
            data = {
                "title": "Test Song",
                "task_id": "mock_task_id_123",
                "genre": "POP",
                "mood": "HAPPY",
                "occasion": "PARTY",
                "voice_tone": "FEMALE",
                "description": "A happy pop song for parties",
                "duration": 180
            }

        elif strategy_name == "suno":
            data = {
                "title": "Test Song Suno",
                "genre": "CLASSICAL",
                "mood": "ROMANTIC",
                "occasion": "RELAXATION",
                "voice_tone": "FEMALE",
                "description": "A romantic classical piece for relaxation"}

        context = SongGenerationContext(strategy)
        song = context.generate_song(user, data)

        # Output result
        self.stdout.write(self.style.SUCCESS(f"Song saved: {song.id}"))
        self.stdout.write(self.style.SUCCESS(f"Title: {song.title}"))
        self.stdout.write(self.style.SUCCESS(f"Audio URL: {song.audio_url}"))
        self.stdout.write(self.style.SUCCESS(f"Status: {song.generation_status}"))