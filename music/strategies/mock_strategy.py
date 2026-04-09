from .base import SongGeneratorStrategy

class MockSongGeneratorStrategy(SongGeneratorStrategy):

    def generate(self, request_data):
        return {
            "audio_url": "https://example.com/mock-song.mp3",
            "status": "SUCCESS",
            "title": request_data['title']
        }