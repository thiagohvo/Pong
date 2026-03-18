import pygame
from config import *

class Raquete:
    def __init__(self, x, y):
        # Define posição inicial da raquete
        self.x = x
        self.y = y

    def mover_cima(self):
        # Move para cima respeitando limite da tela
        if self.y > 0:
            self.y -= VELOCIDADE_RAQUETE

    def mover_baixo(self):
        # Move para baixo respeitando limite da tela
        if self.y < ALTURA - RAQUETE_ALTURA:
            self.y += VELOCIDADE_RAQUETE

    def seguir_bola(self, bola_y):
        # IA simples que segue a bola
        if self.y + RAQUETE_ALTURA // 2 < bola_y:
            self.mover_baixo()
        elif self.y + RAQUETE_ALTURA // 2 > bola_y:
            self.mover_cima()

    def rect(self):
        # Retorna retângulo da raquete para colisão
        return pygame.Rect(self.x, self.y, RAQUETE_LARGURA, RAQUETE_ALTURA)

    def desenhar(self, tela):
        # Desenha a raquete
        pygame.draw.rect(
            tela,
            BRANCO,
            (self.x, self.y, RAQUETE_LARGURA, RAQUETE_ALTURA)
        )