import pygame
from pygame.sprite import Sprite


class BaseItem(Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
