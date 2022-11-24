import pygame.image

from BaseItem import BaseItem

class Bullet(BaseItem):
    window = None

    def __init__(self,tank,window, wallList):
        self.window = window
        self.images = {
            'U': pygame.image.load('images/bulletU.png'),
            'D': pygame.image.load('images/bulletD.png'),
            'L': pygame.image.load('images/bulletL.png'),
            'R': pygame.image.load('images/bulletR.png'),
        }
        self.direction = tank.direction
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2

        self.speed = 6
        # 子弹的状态是否碰到墙壁，碰到墙壁修改此状态
        self.live = True
        self.wallList = wallList

    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 碰到墙壁修改子弹状态
                self.live = False

        elif self.direction == 'R':
            if self.rect.left + self.rect.width < self.window.get_width():
                self.rect.left += self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < self.window.get_height():
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False

    def display_bullet(self):
        self.window.blit(self.image, self.rect)

    def hit_wall(self):
        #循环遍历墙壁列表
        for wall in self.wallList:
            if pygame.sprite.collide_rect(self, wall):
                self.live = False
                wall.hp -= 1
                if wall.hp<=0:
                    wall.live = False


