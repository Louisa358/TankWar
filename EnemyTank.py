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
        self.direction = self.rand_direction()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = speed
        self.flag = True
        self.windows = windows
        self.step = 20

    def rand_direction(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'EU'
        elif num == 2:
            return 'ED'
        elif num == 3:
            return 'EL'
        elif num == 4:
            return 'ER'

    def move(self):
        if self.direction == 'EL':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'EU':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'ER':
            if self.rect.left + self.rect.height < self.windows.get_width():
                self.rect.left += self.speed
        elif self.direction == 'ED':
            if self.rect.top + self.rect.height < self.windows.get_height():
                self.rect.top += self.speed

    def rand_move(self):
        if self.step <= 0:
            self.direction = self.rand_direction()
            self.step = 60
        else:
            self.move()
            self.step -= 1
