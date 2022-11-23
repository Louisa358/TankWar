import pygame.image
from Tank import Tank
import random
from Bullet import Bullet


class EnemyTank(Tank):
    def __init__(self, left, top, speed, windows):
        super(EnemyTank, self).__init__(left, top, windows)
        self.images = {
            'U': pygame.image.load('images/ET-U.png'),
            'D': pygame.image.load('images/ET-D.png'),
            'L': pygame.image.load('images/ET-L.png'),
            'R': pygame.image.load('images/ET-R.png'),
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
        self.live = True

    def rand_direction(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < self.windows.get_width():
                self.rect.left += self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < self.windows.get_height():
                self.rect.top += self.speed

    def rand_move(self):
        if self.step <= 0:
            self.direction = self.rand_direction()
            self.step = 60
        else:
            self.move()
            self.step -= 1

    def shoot(self):
        # 随机生成100以内的数
        num = random.randint(1, 100)
        if num < 10:
            return Bullet(self, self.windows)
