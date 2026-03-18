import pygame
import sys
from config import *

class Menu:
    def __init__(self, tela):
        self.tela = tela

    def mostrar(self):
        # Loop do menu
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Inicia o jogo ao pressionar espaço
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return

            self.tela.fill(PRETO)

            # Título do jogo
            fonte = pygame.font.SysFont(None, 50)
            texto = fonte.render("Pong", True, BRANCO)
            self.tela.blit(texto, texto.get_rect(center=(LARGURA//2, ALTURA//4)))

            # Texto piscando
            fonte2 = pygame.font.SysFont(None, 30)
            tempo = pygame.time.get_ticks()

            if tempo % 2000 < 1000:
                aviso = fonte2.render("Pressione ESPAÇO", True, BRANCO)
                self.tela.blit(aviso, aviso.get_rect(center=(LARGURA//2, ALTURA//2)))

            pygame.display.flip()