from abc import ABC, abstractmethod

class Movivel(ABC):
    @abstractmethod
    def mover(self):
        pass