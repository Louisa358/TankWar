import pygame.image
from Tank import Tank
import random


class EnemyTank(Tank):
    def __init__(self, left, top, speed, windows):
        self.images = {
            'EU': pygame.image.load('images/ET-U.png'),
            'ED': pygame.image.load('images/ET-D.png'),
            'EL': pygame.image.load('images/ET-L.png'),
            'ER': pygame.image.load('images/ET-R.png'),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.flag = True
        self.windows = windows

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'EU'
        elif num == 2:
            return 'ED'
        elif num == 3:
            return 'EL'
        elif num == 4:
            return 'ER'
