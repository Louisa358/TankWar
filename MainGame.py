import pygame
from Tank import Tank

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame:
    window = None
    my_tank = None

    def __init__(self):
        pass

    def start_game(self):
        pygame.display.init()
        self.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('Tank War')
        self.my_tank = Tank(300, 250, self.window)
        while True:
            self.window.fill(BG_COLOR)
            self.getEvent()
            self.window.blit(self.getTextSurface('Enemy Tank left: %d' % 6), (10, 10))
            self.my_tank.display_tank()
            pygame.display.update()

    def end_game(self):
        print('Thanks')
        exit()

    def getTextSurface(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('gadugi', 18)
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.my_tank.direction = 'L'
                    self.my_tank.move()
                elif event.key == pygame.K_RIGHT:
                    self.my_tank.direction = 'R'
                    self.my_tank.move()
                elif event.key == pygame.K_UP:
                    self.my_tank.direction = 'U'
                    self.my_tank.move()
                elif event.key == pygame.K_DOWN:
                    self.my_tank.direction = 'D'
                    self.my_tank.move()


if __name__ == '__main__':
    MainGame().start_game()
