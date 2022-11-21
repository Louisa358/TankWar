import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0,0,0)
TEXT_COLOR = pygame.Color(255,0,0)

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
            self.getEvent()
            self.window.blit(self.getTextSurface('Enemy Tank left: %d' %6),(10,10))
            pygame.display.update()



    def end_game(self):
        print('Thanks')
        exit()

    def getTextSurface(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('gadugi',18)
        textSurface = font.render(text,True,TEXT_COLOR)
        return textSurface

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_UP:
                    pass
                elif event.key == pygame.K_DOWN:
                    pass


if __name__=='__main__':
    MainGame().start_game()