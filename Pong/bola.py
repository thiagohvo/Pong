import pygame
from config import *

class Bola:
    def __init__(self):
        # Inicializa a bola no centro
        self.reset()

    def reset(self):
        # Reseta posição e velocidade da bola
        self.x = LARGURA // 2
        self.y = ALTURA // 2
        self.vx = VELOCIDADE_BOLA
        self.vy = VELOCIDADE_BOLA

    def mover(self):
        # Atualiza posição da bola
        self.x += self.vx
        self.y += self.vy

        # Verifica colisão com topo e base
        if self.y <= 0 or self.y >= ALTURA:
            self.vy *= -1  # inverte direção vertical

    def colidir(self, raquete1, raquete2):
        # Verifica colisão com as raquetes
        if self.rect().colliderect(raquete1.rect()) or \
           self.rect().colliderect(raquete2.rect()):
            self.vx *= -1  # inverte direção horizontal

    def ponto(self):
        # Verifica se alguém marcou ponto
        if self.x <= 0:
            return "player2"
        if self.x >= LARGURA:
            return "player1"
        return None

    def rect(self):
        # Retorna um retângulo para colisão
        return pygame.Rect(self.x, self.y, BOLA_TAMANHO, BOLA_TAMANHO)

    def desenhar(self, tela):
        # Desenha a bola na tela
        pygame.draw.circle(tela, BRANCO, (self.x, self.y), BOLA_TAMANHO)