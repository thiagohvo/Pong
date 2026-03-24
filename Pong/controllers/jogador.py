import pygame


class Jogador:
    """
    Controla a raquete do jogador humano usando teclado.
    """

    def __init__(self, raquete):
        self.raquete = raquete

    def atualizar(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_UP]:
            self.raquete.mover_cima()

        if teclas[pygame.K_DOWN]:
            self.raquete.mover_baixo()