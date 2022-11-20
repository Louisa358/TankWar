import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)

class MainGame:
    window = None

    def __init__(self):
        pass

    def start_game(self):
        pygame.display.init()
        self.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('Tank War')
        while True:
            self.window.fill(BG_COLOR)
            pygame.display.update()


    def end_game(self):
        pass


if __name__=='__main__':
    MainGame().start_game()