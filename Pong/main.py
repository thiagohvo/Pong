import pygame
from config import *
from game import Game
from menu import Menu

def main():
    pygame.init()

    # Cria janela
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Pong")

    # Instancia objetos principais
    menu = Menu(tela)
    game = Game(tela)

    # Loop geral
    while True:
        menu.mostrar()  # mostra menu
        game.rodar()    # inicia jogo

    pygame.quit()


if __name__ == "__main__":
    main()