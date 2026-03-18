import pygame
from config import *
from bola import Bola
from raquete import Raquete

class Game:
    def __init__(self, tela):
        self.tela = tela
        self.clock = pygame.time.Clock()

        # Cria objetos do jogo
        self.bola = Bola()
        self.player1 = Raquete(15, ALTURA//2)
        self.player2 = Raquete(LARGURA - 25, ALTURA//2)

        # Pontuação
        self.score1 = 0
        self.score2 = 0

    def processar_input(self):
        # Captura teclas do jogador
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player1.mover_cima()
        if keys[pygame.K_DOWN]:
            self.player1.mover_baixo()

    def atualizar(self):
        # Atualiza estado do jogo
        self.bola.mover()
        self.bola.colidir(self.player1, self.player2)

        # IA do player 2
        self.player2.seguir_bola(self.bola.y)

        # Verifica pontuação
        ponto = self.bola.ponto()
        if ponto:
            if ponto == "player1":
                self.score1 += 1
            else:
                self.score2 += 1

            self.bola.reset()

    def desenhar(self):
        # Renderiza tudo
        self.tela.fill(PRETO)

        self.bola.desenhar(self.tela)
        self.player1.desenhar(self.tela)
        self.player2.desenhar(self.tela)

        # Mostra placar
        fonte = pygame.font.SysFont(None, 36)
        texto = fonte.render(f"{self.score1} - {self.score2}", True, BRANCO)
        self.tela.blit(texto, texto.get_rect(center=(LARGURA//2, 30)))

        pygame.display.flip()

    def rodar(self):
        # Loop principal do jogo
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return

            self.processar_input()
            self.atualizar()
            self.desenhar()

            self.clock.tick(FPS)