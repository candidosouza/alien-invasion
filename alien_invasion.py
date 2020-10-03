import sys
import pygame
import typing

from settings import Settings


def run_game() -> None:
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    settings = Settings()

    screen: pygame.SurfaceType = pygame.display.set_mode(
        (settings.screen_width, settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

    # Inicia o laço principal do jogo
    while True:

        # Observa os eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem do laço for
        screen.fill(settings.bg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()