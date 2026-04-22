from urllib import response

import requests
from .base import SongGeneratorStrategy
from django.conf import settings
import time

class SunoSongGeneratorStrategy(SongGeneratorStrategy):

    BASE_URL = "https://api.sunoapi.org/api/v1"
    SUCCESS_STATUS = {"SUCCESS"}
    PENDING_STATUS = {"PENDING", "TEXT_SUCCESS"}
    FAILED_STATUS = {
        "CREATE_TASK_FAILED",
        "GENERATE_AUDIO_FAILED",
        "CALLBACK_EXCEPTION",
        "SENSITIVE_WORD_ERROR",
    }

    def build_prompt(self, data):
        return f"""
        A {data['mood']} {data['genre']} song for {data['occasion']} 
        with a {data['voice_tone']} voice.
        {data.get('description', '')}
        """.strip()

    def generate(self, request_data):
        headers = {
            "Authorization": f"Bearer {settings.SUNO_API_KEY}",
            "Content-Type": "application/json"
        }
        prompt = self.build_prompt(request_data)

        request_data = {
            "prompt": prompt,
            "style": request_data["genre"],
            "title": request_data["title"],
            "customMode": False,
            "instrumental": False,
            "model": "V4_5ALL",
            "callBackUrl": "https://example.com/callback"
        }


        response = requests.post(
            f"{self.BASE_URL}/generate",
            json=request_data,
            headers=headers
        )

        print("Suno API response:", response.status_code, response.text)

        data = response.json()
        task_id = data['data']['taskId']

        for _ in range(100):  
            time.sleep(10) 
            result = self.check_status(task_id)
            # print(result)
            if result:
                return {
                    "audio_url": result.get("audio_url"),
                    "title": result.get("title"),
                    "duration": result.get("duration"),
                    "task_id": task_id,
                    "status": result.get("status")
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
            audio_data = result['data']['response']['sunoData'][0]
            print(f"Audio URL: {audio_data.get('audioUrl')}")
            print(f"Title: {audio_data.get('title')}")
            return {
                "status": "SUCCESS",
                "task_id": task_id,
                "audio_url": audio_data.get("audioUrl"),
                "title": audio_data.get("title"),
                "duration": audio_data.get("duration"),
            }
            # return audio_data
        elif status in self.PENDING_STATUS:
            print("Still generating...")
            return None
        elif status in self.FAILED_STATUS:
            print(f"Generation failed with status: {status}")
            return None
        else:
            print(f"Generation: {status}")
            return None