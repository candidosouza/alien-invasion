import sys
import pygame


def check_events():
    """ Responde a eventos de pressionamento de teclas e mouse """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    """ Atualiza as imagens na tela e alterna para uma nova tela """
    # Redesenha a tela a cada passagem do laço
    screen.fill(settings.bg_color)
    ship.blitme()

    # Deixa a tela mais recente visível
    pygame.display.flip()