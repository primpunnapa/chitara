from .base import SongGeneratorStrategy

class MockSongGeneratorStrategy(SongGeneratorStrategy):

    def generate(self, request_data):
        return {
            "audio_url": "https://example.com/mock-song.mp3",
            "status": "SUCCESS",
            "title": request_data['title'],
            "task_id": request_data['task_id'],
            "genre": request_data['genre'],
            "mood": request_data['mood'],
            "occasion": request_data['occasion'],
            "voice_tone": request_data['voice_tone'],
            "duration": request_data.get("duration")
        }
    
    def check_status(self, task_id):
        return {
            "data": {
                "status": "SUCCESS",
                "response": {
                    "data": [
                        {
                            "audio_url": "https://example.com/mock-song.mp3",
                            "title": "Mock Song"
                        }
                    ]
                }
            }
        }