import pygame
import sys
from game import Game


def main():
    pygame.init()

    largura = 800
    altura = 600

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Pong")

    game = Game(tela)   # 👈 PASSANDO A TELA
    game.run()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()