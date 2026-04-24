from .base import SongGeneratorStrategy

class MockSongGeneratorStrategy(SongGeneratorStrategy):

    def generate(self, request_data):
        return {
            "audio_url": "https://tempfile.aiquickdraw.com/r/dd74fddfff28484ba0b2f198b1ef1a9a.mp3",
            "status": "SUCCESS",
            "title": request_data['title'],
            "task_id": request_data['task_id'] if 'task_id' in request_data else "mock_task_id_123",
            "genre": request_data['genre'],
            "mood": request_data['mood'],
            "occasion": request_data['occasion'],
            "voice_tone": request_data['voice_tone'],
            "duration": 152.72
        }
