import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game() -> None:
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    settings = Settings()

    screen: pygame.SurfaceType = pygame.display.set_mode(
        (settings.screen_width, settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")

    # cria a espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, ship)


run_game()
