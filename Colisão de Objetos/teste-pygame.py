import pygame
import sys
import random

pygame.init()

# CONFIG
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
LARGURA = 800
ALTURA = 600
FPS = 60
TAMANHO_FONTE = 50

TEXTO1 = "GEROMEL"
TEXTO2 = "KANNEMANN"

# FUNÇÕES
def gerar_velocidade():
    vx = random.choice([-3, -2, 2, 3])
    vy = random.choice([-3, -2, 2, 3])
    return vx, vy

def cor_aleatoria():
    return (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255),
    )

def criar_texto(fonte, texto, cor, pos):
    surf = fonte.render(texto, True, cor)
    rect = surf.get_rect(center=pos)
    return surf, rect

def colisao_borda(rect, vx, vy):
    mudou = False

    if rect.right >= LARGURA or rect.left <= 0:
        vx *= -1
        mudou = True

    if rect.bottom >= ALTURA or rect.top <= 0:
        vy *= -1
        mudou = True

    return vx, vy, mudou

# MAIN
def main():
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Texto Maluco 😄")

    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont(None, TAMANHO_FONTE)

    texto1, rect1 = criar_texto(fonte, TEXTO1, BRANCO, (200, 300))
    texto2, rect2 = criar_texto(fonte, TEXTO2, BRANCO, (600, 300))

    vx1, vy1 = gerar_velocidade()
    vx2, vy2 = gerar_velocidade()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # MOVIMENTO
        rect1.x += vx1
        rect1.y += vy1
        rect2.x += vx2
        rect2.y += vy2

        # COLISÃO COM BORDA
        vx1, vy1, mudou1 = colisao_borda(rect1, vx1, vy1)
        vx2, vy2, mudou2 = colisao_borda(rect2, vx2, vy2)

        if mudou1:
            texto1 = fonte.render(TEXTO1, True, cor_aleatoria())
        if mudou2:
            texto2 = fonte.render(TEXTO2, True, cor_aleatoria())

        # COLISÃO ENTRE TEXTOS
        if rect1.colliderect(rect2):
            vx1, vx2 = vx2, vx1
            vy1, vy2 = vy2, vy1

            texto1 = fonte.render(TEXTO1, True, cor_aleatoria())
            texto2 = fonte.render(TEXTO2, True, cor_aleatoria())

        # DESENHO
        tela.fill(PRETO)
        tela.blit(texto1, rect1)
        tela.blit(texto2, rect2)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

main()