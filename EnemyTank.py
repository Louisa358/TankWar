import pygame.image
from Tank import Tank
import random

class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        self.images = {
            'EU': pygame.image.load('images/ET-U.png'),
            'ED': pygame.image.load('images/MT-D.png'),
            'EL': pygame.image.load('images/MT-L.png'),
            'ER': pygame.image.load('images/MT-R.png'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.flag = True

    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'