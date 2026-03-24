from abc import ABC, abstractmethod

class Renderizavel(ABC):
    @abstractmethod
    def desenhar(self, tela):
        pass