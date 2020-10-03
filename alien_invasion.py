import sys
import pygame
import typing


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()

    screen: pygame.SurfaceType = pygame.display.set_mode((1200, 768))
    pygame.display.set_caption("Alien Invasion")

    print(type(screen))

    # define a cor de fundo
    bg_color: tuple = (230, 230, 230)

    # Inicia o laço principal do jogo
    while True:

        # Observa os eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem do laço for
        screen.fill(bg_color)

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()