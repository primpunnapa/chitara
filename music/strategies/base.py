from abc import ABC, abstractmethod

class SongGeneratorStrategy(ABC):

    @abstractmethod
    def generate(self, request_data):
        pass