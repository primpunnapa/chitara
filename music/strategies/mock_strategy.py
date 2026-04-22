from .base import SongGeneratorStrategy

class MockSongGeneratorStrategy(SongGeneratorStrategy):

    def generate(self, request_data):
        return {
            "audio_url": "https://example.com/mock-song.mp3",
            "status": "SUCCESS",
            "title": request_data['title']
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