import random
import time
import pygame
from pygame.sprite import Sprite
from Bullet import Bullet
from EnemyTank import EnemyTank
from Explode import Explode
from Tank import Tank
from Wall import Wall

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


class MainGame:
    window = None
    my_tank = None
    enemyTankList = []
    enemyTankCount = 5
    myBulletList = []
    enemyBulletList = []
    bullets = myBulletList + enemyBulletList
    explodeList = []
    wallList = []

    def start_game(self):
        time.sleep(0.02)
        pygame.display.init()
        self.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.create_my_tank()
        pygame.display.set_caption('Tank War')
        self.my_tank = Tank(300, 250, self.window)
        self.create_enemy_tank()
        self.create_wall()

        while True:
            time.sleep(0.02)
            self.window.fill(BG_COLOR)
            self.getEvent()
            self.window.blit(self.get_text_surface('Enemy Tank left: %d' % len(self.enemyTankList)), (10, 10))
            if self.my_tank and self.my_tank.live:
                self.my_tank.displayTank()
            else:
                del self.my_tank
                self.my_tank = None
            self.blit_enemy_tank()
            self.blit_my_bullet()
            self.blit_enemy_bullet()
            self.blit_explode()
            self.blit_wall()
            if self.my_tank and self.my_tank.live:
                if not self.my_tank.stop:
                    self.my_tank.move()
                    # MainGame.my_tank.hitWall()
                    # self.my_tank.mytank_hit_enemytank()

            pygame.display.update()

    def blit_wall(self):
        for wall in self.wallList:
            if wall.live:
                wall.displayWall()
            else:
                self.wallList.remove(wall)

    def create_wall(self):
        for i in range(6):
            wall = Wall(i*130,220,self.window)
            self.wallList.append(wall)

    def create_my_tank(self):
        self.my_tank = Tank(300, 250, self.window)


    def create_enemy_tank(self):
        top = 100
        for i in range(self.enemyTankCount):
            left = random.randint(0, 600)
            speed = random.randint(1, 4)
            enemy = EnemyTank(left, top, speed, self.window, self.wallList)
            self.enemyTankList.append(enemy)

    def blit_enemy_tank(self):
        for enemyTank in self.enemyTankList:
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.rand_move()
                enemyBullet = enemyTank.shoot()
                if enemyBullet:
                    self.enemyBulletList.append(enemyBullet)
            else:
                self.enemyTankList.remove(enemyTank)

    def blit_my_bullet(self):
        for myBullet in self.myBulletList:
            if myBullet.live:
                myBullet.display_bullet()
                myBullet.move()
                self.mybullet_hit_enemytank(myBullet)
                myBullet.hit_wall()
            else:
                self.myBulletList.remove(myBullet)

    def blit_enemy_bullet(self):
        for enemyBullet in self.enemyBulletList:
            if enemyBullet.live:
                enemyBullet.display_bullet()
                enemyBullet.move()
                self.enemybullet_hit_mytank(enemyBullet)
                enemyBullet.hit_wall()
            else:
                self.enemyBulletList.remove(enemyBullet)

    def blit_explode(self):
        for explode in self.explodeList:
            if explode.live:
                explode.display_explode()
            else:
                self.explodeList.remove(explode)

    def mybullet_hit_enemytank(self, myBullet):
        for enemytank in self.enemyTankList:
            if pygame.sprite.collide_rect(enemytank, myBullet):
                enemytank.live = False
                myBullet.live = False
                explode = Explode(enemytank,self.window)
                self.explodeList.append(explode)

    def enemybullet_hit_mytank(self,enemybullet):
        if self.my_tank and self.my_tank.live:
            if pygame.sprite.collide_rect(self.my_tank,enemybullet):
                explode = Explode(self.my_tank,self.window)
                self.explodeList.append(explode)
                enemybullet.live = False
                self.my_tank.live = False

    def end_game(self):
        print('Thanks')
        exit()

    def get_text_surface(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('gadugi', 18)
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if not self.my_tank:
                    if event.key == pygame.K_ESCAPE:
                        self.create_my_tank()
                if self.my_tank and self.my_tank.live:
                    if event.key == pygame.K_LEFT:
                        self.my_tank.direction = 'L'
                        self.my_tank.stop = False
                    elif event.key == pygame.K_RIGHT:
                        self.my_tank.direction = 'R'
                        self.my_tank.stop = False
                    elif event.key == pygame.K_UP:
                        self.my_tank.direction = 'U'
                        self.my_tank.stop = False
                    elif event.key == pygame.K_DOWN:
                        self.my_tank.direction = 'D'
                        self.my_tank.stop = False
                    elif event.key == pygame.K_SPACE:
                        if len(self.myBulletList) < 3:
                            myBullet = Bullet(self.my_tank, self.window, self.wallList)
                            self.myBulletList.append(myBullet)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    if self.my_tank and self.my_tank.live:
                        self.my_tank.stop = True

if __name__ == '__main__':
    MainGame().start_game()
