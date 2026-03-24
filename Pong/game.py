import pygame
import pygame.mixer

from entidades.bola import Bola
from entidades.raquete import Raquete

from config import PRETO, BRANCO, LARGURA, ALTURA, FPS


class Game:
    """
    Classe principal do jogo.
    Responsável por controlar lógica, física, áudio e renderização.
    """

    def __init__(self, tela):

        self.tela = tela
        self.clock = pygame.time.Clock()

        # ---------------------------
        # INICIALIZA SISTEMA DE ÁUDIO
        # ---------------------------

        pygame.mixer.init()

        # Carrega efeitos sonoros
        self.som_raquete = pygame.mixer.Sound("audio/hit_raquete.mp3")
        self.som_parede = pygame.mixer.Sound("audio/hit_parede.mp3")
        self.som_gol = pygame.mixer.Sound("audio/gol.mp3")

        # Carrega música de fundo
        pygame.mixer.music.load("audio/musica.mp3")

        # Define volume da música
        pygame.mixer.music.set_volume(0.3)

        # Toca música em loop infinito
        pygame.mixer.music.play(-1)

        # ---------------------------
        # SISTEMA DE BOLAS
        # ---------------------------

        # Lista de bolas (começa com apenas a bola verdadeira)
        self.bolas = [Bola(True)]

        # Controle de tempo do power-up
        self.ultimo_powerup = pygame.time.get_ticks()

        # ---------------------------
        # RAQUETES
        # ---------------------------

        self.player1 = Raquete(15, ALTURA // 2)
        self.player2 = Raquete(LARGURA - 25, ALTURA // 2)

        # ---------------------------
        # PLACAR
        # ---------------------------

        self.score1 = 0
        self.score2 = 0

    def processar_input(self):
        """
        Captura input do jogador
        """

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player1.mover_cima()

        if keys[pygame.K_DOWN]:
            self.player1.mover_baixo()

    def atualizar(self):
        """
        Atualiza toda a lógica do jogo
        """

        for bola in self.bolas:

            # ---------------------------
            # MOVIMENTO DA BOLA
            # ---------------------------

            # mover bola e verificar colisão com parede
            bateu_parede = bola.mover()

            if bateu_parede:
                self.som_parede.play()

            # ---------------------------
            # COLISÃO COM RAQUETES
            # ---------------------------

            colidiu = bola.colidir(self.player1, self.player2)

            if colidiu:
                self.som_raquete.play()

            # ---------------------------
            # IA SEGUE BOLA VERDADEIRA
            # ---------------------------

            if bola.verdadeira:
                self.player2.seguir_bola(bola.y)

            # ---------------------------
            # POWER-UP MULTI-BOLA
            # ---------------------------

            agora = pygame.time.get_ticks()

            # a cada 5 segundos + colisão gera novas bolas
            if colidiu and agora - self.ultimo_powerup > 5000:

                self.ultimo_powerup = agora

                for _ in range(4):

                    nova = Bola(False)

                    # nova bola nasce na posição da bola original
                    nova.x = bola.x
                    nova.y = bola.y

                    self.bolas.append(nova)

            # ---------------------------
            # VERIFICA PONTUAÇÃO
            # ---------------------------

            ponto = bola.ponto()

            if ponto:

                # toca som de gol
                self.som_gol.play()

                if ponto == "player1":
                    self.score1 += 1
                else:
                    self.score2 += 1

                # reinicia jogo com apenas a bola verdadeira
                self.bolas = [Bola(True)]

                break

    def desenhar(self):
        """
        Renderiza todos os elementos do jogo
        """

        # limpa tela
        self.tela.fill(PRETO)

        # desenha bolas
        for bola in self.bolas:
            bola.desenhar(self.tela)

        # desenha raquetes
        self.player1.desenhar(self.tela)
        self.player2.desenhar(self.tela)

        # ---------------------------
        # DESENHA PLACAR
        # ---------------------------

        fonte = pygame.font.SysFont(None, 36)

        texto = fonte.render(
            f"{self.score1} - {self.score2}",
            True,
            BRANCO
        )

        self.tela.blit(
            texto,
            texto.get_rect(center=(LARGURA // 2, 30))
        )

        pygame.display.flip()

    def run(self):
        """
        Loop principal do jogo
        """

        while True:

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:
                    return

            self.processar_input()
            self.atualizar()
            self.desenhar()

            self.clock.tick(FPS)