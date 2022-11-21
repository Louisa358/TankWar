import pygame


class Tank:
    windows = None

    def __init__(self, left, top, windows):
        self.images = {
            'U': pygame.image.load('images/MT-U.png'),
            'D': pygame.image.load('images/MT-D.png'),
            'L': pygame.image.load('images/MT-L.png'),
            'R': pygame.image.load('images/MT-R.png'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 6
        self.windows = windows

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'R':
            if self.rect.
                self.rect.left += self.speed
        elif self.direction == 'D':
            self.rect.top += self.speed

    def shoot(self):
        pass

    def display_tank(self):
        self.image = self.images[self.direction]
        self.windows.blit(self.image, self.rect)
