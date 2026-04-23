from django.conf import settings
from .mock_strategy import MockSongGeneratorStrategy
from .suno_strategy import SunoSongGeneratorStrategy

def get_generator_strategy(strategy_name=None):
    strategy_name = (
        strategy_name
        or getattr(settings, "GENERATOR_STRATEGY", "suno")
    ).lower()

    if strategy_name == "mock":
        return MockSongGeneratorStrategy()
    elif strategy_name == "suno":
        return SunoSongGeneratorStrategy()
    
    return SunoSongGeneratorStrategy()