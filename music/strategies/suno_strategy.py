from urllib import response

import requests
from .base import SongGeneratorStrategy
from django.conf import settings
import time

class SunoSongGeneratorStrategy(SongGeneratorStrategy):

    BASE_URL = "https://api.sunoapi.org/api/v1"
    SUCCESS_STATUS = {"SUCCESS"}
    FAILED_STATUS = {
        "CREATE_TASK_FAILED",
        "GENERATE_AUDIO_FAILED",
        "CALLBACK_EXCEPTION",
        "SENSITIVE_WORD_ERROR"
    }

    def generate(self, request_data):
        headers = {
            "Authorization": f"Bearer {settings.SUNO_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            f"{self.BASE_URL}/generate",
            json=request_data,
            headers=headers
        )

        print("Suno API response:", response.status_code, response.text)

        data = response.json()
        task_id = data['data']['taskId']

        for _ in range(30):  
            time.sleep(5) 
            result = self.check_status(task_id)
            print(result)
            if result is not None:
                return {
                    "audio_url": result['data']['response']['data'][0]['audio_url'], 
                    "title": result['data']['response']['data'][0]['title'],
                    "task_id": task_id,
                    "status": result['data']['status']
                }

        return {
            "task_id": task_id,
            "status": "FAILED"
        }
    
    def check_status(self, task_id):
        url = f"{self.BASE_URL}/generate/record-info?taskId={task_id}"
        headers = {"Authorization": f"Bearer {settings.SUNO_API_KEY}"}

        response = requests.get(url, headers=headers)
        result = response.json()
        status = result['data']['status']

        if status == 'SUCCESS':
            print("Generation complete!")
            audio_data = result['data']['response']['data']
            for i, audio in enumerate(audio_data):
                print(f"Track {i+1}: {audio['audio_url']}")
            return audio_data
        elif status == 'GENERATING':
            print("Still generating...")
            return None
        else:
            print(f"Generation failed: {status}")
            return None