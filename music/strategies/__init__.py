from django.conf import settings
from .mock_strategy import MockSongGeneratorStrategy
from .suno_strategy import SunoSongGeneratorStrategy

def get_generator_strategy():
    if settings.GENERATOR_STRATEGY == "suno":
        return SunoSongGeneratorStrategy()
    return MockSongGeneratorStrategy()