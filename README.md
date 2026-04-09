# Chitara

The Chitara project is a AI-powered song generation created by Django-based application that provides a backend for managing users, libraries, and songs. It includes features such as user authentication, song generation limits, and CRUD operations for the main domain models.

# prerequisites
- Python 3.8+

## Setup
1. Create virtual environment & Install Django
```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
```
2. Run migrations:
```bash
   python manage.py migrate
```
3. Run server:
```bash
   python manage.py runserver
```
open server at http://127.0.0.1:8000/

4. (Optional) Create a superuser:
```bash
   python manage.py createsuperuser
```
## How to use strategies
1. go to termial and run python shell
```bash
   python manage.py shell
```
2. To use mock strategy and generate a song
```python
from music.strategies.mock_strategy import MockSongGeneratorStrategy
strategy = MockSongGeneratorStrategy()

data = {
    "title": "mock song",
    "audio_url" : "https://example.com/mock-song.mp3"
}

strategy.generate(data)
```
3. To use suno strategy and generate a song
```python
from music.strategies.suno_strategy import SunoSongGeneratorStrategy

strategy = SunoSongGeneratorStrategy()

data = {
    "prompt": "A calm and relaxing piano track with soft melodies",
    "style": "Classical",
    "title": "Peaceful Piano Meditation",
    "customMode": False,
    "instrumental": True,
    "model": "V4_5ALL",
    "callBackUrl": "https://example.com/callback" 
}
strategy.generate(data)
```
## Features
- User, Library, Song domain models
- Enum-based attributes
- CRUD via Django Admin

## Demo CRUD video
![CRUD Demo](./demo.mp4)