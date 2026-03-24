import pygame
import random
from config import *


class Bola:
    """
    Classe responsável por representar a bola no jogo.
    Pode ser uma bola verdadeira (pontua) ou falsa (apenas distração).
    """

    def __init__(self, verdadeira=True):
        # Define se a bola é a verdadeira (capaz de marcar ponto)
        self.verdadeira = verdadeira

        # Bola verdadeira é branca, bolas falsas recebem cor aleatória
        self.cor = BRANCO if verdadeira else self.cor_aleatoria()

        # Inicializa posição e velocidade
        self.reset()

    def cor_aleatoria(self):
        """
        Gera uma cor RGB aleatória.
        Usado para criar bolas falsas com cores diferentes.
        """

        return (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def reset(self):
        """
        Reinicia posição da bola no centro da tela
        e define velocidade inicial aleatória.
        """

        self.x = LARGURA // 2
        self.y = ALTURA // 2

        # velocidade inicial aleatória para esquerda ou direita
        self.vx = random.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA])
        self.vy = random.choice([-VELOCIDADE_BOLA, VELOCIDADE_BOLA])

    def mover(self):
        """
        Atualiza posição da bola e trata colisão com
        as paredes superior e inferior.
        """

        self.x += self.vx
        self.y += self.vy

        # colisão com topo ou base
        if self.y <= 0 or self.y >= ALTURA:

            # inverte direção vertical
            self.vy *= -1

            # adiciona pequena variação aleatória
            self.vy += random.randint(-3, 3)

    def colidir(self, r1, r2):
        """
        Verifica colisão com as raquetes.
        Retorna True se houve colisão.
        """

        if self.rect().colliderect(r1.rect()) or \
           self.rect().colliderect(r2.rect()):

            # inverte direção horizontal
            self.vx *= -1

            # rebote variável
            self.vy += random.randint(-4, 4)

            # limita velocidade para não quebrar o jogo
            self.vy = max(-10, min(10, self.vy))

            return True

        return False

    def ponto(self):
        """
        Verifica se a bola marcou ponto.
        Apenas a bola verdadeira pode pontuar.
        """

        if not self.verdadeira:
            return None

        if self.x <= 0:
            return "player2"

        if self.x >= LARGURA:
            return "player1"

        return None

    def rect(self):
        """
        Retorna o retângulo de colisão da bola.
        """

        return pygame.Rect(self.x, self.y, BOLA_TAMANHO, BOLA_TAMANHO)

    def desenhar(self, tela):
        """
        Desenha a bola na tela.
        """

        pygame.draw.circle(
            tela,
            self.cor,
            (self.x, self.y),
            BOLA_TAMANHO
        )