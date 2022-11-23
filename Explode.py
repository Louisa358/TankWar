import pygame

class Explode:
    def __init__(self,tank,window):
        self.rect = tank.rect
        self.images = [
            pygame.image.load('images/e1.gif'),
            pygame.image.load('images/e2.gif'),
            pygame.image.load('images/e3.gif'),
            pygame.image.load('images/e4.gif'),
            pygame.image.load('images/e5.gif'),
        ]
        self.step = 0
        self.image = self.images[self.step]
        self.live = True
        self.window = window

    def display_explode(self):
        if self.step < len(self.images):
            self.image = self.images[self.step]
            self.step += 1
            self.window.blit(self.image,self.rect)
        else:
            self.live = False
            self.step = 0