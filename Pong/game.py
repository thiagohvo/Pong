import pygame

from entidades.bola import Bola
from entidades.raquete import Raquete

from config import PRETO, BRANCO, LARGURA, ALTURA, FPS


class Game:
    """
    Classe principal do jogo.
    Responsável por controlar lógica, física e renderização.
    """

    def __init__(self, tela):

        self.tela = tela
        self.clock = pygame.time.Clock()

        # Lista de bolas do jogo (inicia com apenas a bola verdadeira)
        self.bolas = [Bola(True)]

        # Controle de tempo para ativar o power-up
        self.ultimo_powerup = pygame.time.get_ticks()

        # Cria raquetes dos jogadores
        self.player1 = Raquete(15, ALTURA // 2)
        self.player2 = Raquete(LARGURA - 25, ALTURA // 2)

        # Pontuação
        self.score1 = 0
        self.score2 = 0

    def processar_input(self):
        """Captura input do jogador"""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player1.mover_cima()

        if keys[pygame.K_DOWN]:
            self.player1.mover_baixo()

    def atualizar(self):
        """Atualiza estado do jogo"""

        for bola in self.bolas:

            # move bola
            bola.mover()

            # verifica colisão com raquetes
            colidiu = bola.colidir(self.player1, self.player2)

            # IA segue apenas a bola verdadeira
            if bola.verdadeira:
                self.player2.seguir_bola(bola.y)

            # verifica tempo atual
            agora = pygame.time.get_ticks()

            # power-up: a cada 5 segundos + colisão
            if colidiu and agora - self.ultimo_powerup > 5000:

                self.ultimo_powerup = agora

                # cria 4 bolas falsas
                for _ in range(4):

                    nova = Bola(False)

                    # nasce na posição da bola que colidiu
                    nova.x = bola.x
                    nova.y = bola.y

                    self.bolas.append(nova)

            # verifica pontuação
            ponto = bola.ponto()

            if ponto:

                if ponto == "player1":
                    self.score1 += 1
                else:
                    self.score2 += 1

                # reinicia jogo com apenas a bola verdadeira
                self.bolas = [Bola(True)]

    def desenhar(self):
        """Renderiza elementos na tela"""

        self.tela.fill(PRETO)

        # desenha todas as bolas
        for bola in self.bolas:
            bola.desenhar(self.tela)

        self.player1.desenhar(self.tela)
        self.player2.desenhar(self.tela)

        # Placar
        fonte = pygame.font.SysFont(None, 36)
        texto = fonte.render(f"{self.score1} - {self.score2}", True, BRANCO)

        self.tela.blit(texto, texto.get_rect(center=(LARGURA // 2, 30)))

        pygame.display.flip()

    def run(self):
        """Loop principal do jogo"""

        while True:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return

            self.processar_input()
            self.atualizar()
            self.desenhar()

            self.clock.tick(FPS)