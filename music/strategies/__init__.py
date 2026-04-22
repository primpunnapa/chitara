from django.conf import settings
from .mock_strategy import MockSongGeneratorStrategy
from .suno_strategy import SunoSongGeneratorStrategy

def get_generator_strategy(strategy_name=None):
    if strategy_name == "mock":
        return MockSongGeneratorStrategy()
    elif strategy_name == "suno":
        return SunoSongGeneratorStrategy()
    else:
        raise ValueError("Invalid strategy")