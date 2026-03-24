import pygame
import random
from config import *


class Bola:
    def __init__(self):
        """
        Construtor da classe Bola.
        Apenas chama o método reset para iniciar a bola no centro da tela.
        """
        self.reset()

    def reset(self):
        """
        Reinicia a posição da bola no centro da tela
        e define a velocidade inicial.
        """
        self.x = LARGURA // 2
        self.y = ALTURA // 2

        # velocidade inicial da bola
        self.vx = VELOCIDADE_BOLA
        self.vy = VELOCIDADE_BOLA

    def mover(self):
        """
        Atualiza a posição da bola a cada frame.
        Também verifica colisão com as paredes superior e inferior.
        """

        # Atualiza posição com base na velocidade
        self.x += self.vx
        self.y += self.vy

        # Verifica colisão com topo ou base da tela
        if self.y <= 0 or self.y >= ALTURA:

            # Inverte direção vertical
            self.vy *= -1

            # Adiciona uma pequena variação aleatória no rebote
            # Isso evita movimentos totalmente previsíveis
            self.vy += random.randint(-3, 3)

    def colidir(self, raquete1, raquete2):
        """
        Verifica colisão da bola com as raquetes dos jogadores.
        Se ocorrer colisão, a direção horizontal da bola é invertida
        e uma variação aleatória é aplicada na velocidade vertical.
        """

        # colisão com raquete 1
        if self.rect().colliderect(raquete1.rect()):

            # inverte direção horizontal
            self.vx *= -1

            # rebote variável
            self.vy += random.randint(-4, 4)

        # colisão com raquete 2
        if self.rect().colliderect(raquete2.rect()):

            # inverte direção horizontal
            self.vx *= -1

            # rebote variável
            self.vy += random.randint(-4, 4)

        # Limita a velocidade vertical para evitar que a bola fique rápida demais
        self.vy = max(-10, min(10, self.vy))

    def ponto(self):
        """
        Verifica se algum jogador marcou ponto.
        Se a bola ultrapassar as laterais da tela,
        retorna qual jogador pontuou.
        """

        if self.x <= 0:
            return "player2"

        if self.x >= LARGURA:
            return "player1"

        return None

    def rect(self):
        """
        Retorna um retângulo que representa a área de colisão da bola.
        Isso facilita a detecção de colisão com as raquetes.
        """

        return pygame.Rect(self.x, self.y, BOLA_TAMANHO, BOLA_TAMANHO)

    def desenhar(self, tela):
        """
        Desenha a bola na tela utilizando pygame.
        """

        pygame.draw.circle(
            tela,
            BRANCO,
            (self.x, self.y),
            BOLA_TAMANHO
        )