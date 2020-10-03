class Settings():
    """ Uma classe para armazenar todas as configurações do jogo """

    def __init__(self):
        """ Inicializa as configurações do jogo """

        # Configurações de tela
        self.screen_width: int = 1200
        self.screen_heigth: int = 800
        self.bg_color: tuple = (230, 230, 230)
