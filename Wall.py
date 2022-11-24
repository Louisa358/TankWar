import pygame

class Wall:
    window = None
    def __init__(self,left,top,window):
        self.window = window
        self.image = pygame.image.load('images/wall.jpg')
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.live = True
        self.hp = 3

    def displayWall(self):
        self.window.blit(self.image, self.rect)

