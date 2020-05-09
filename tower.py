import pygame as pg
import random as r

from config import *

class Tower():
    def __init__(self, pos, entities, field_coords, lvl=1):
        self.image = pg.Surface((SCALE, SCALE)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.font = pg.font.SysFont('comicsansms', int(SCALE*.75))

        self.entities = entities
        self.delay = 500
        self.timer = 0
        self.dmg = 5
        self.lvl = lvl

        self.field_coords = field_coords

    def draw(self):
        self.image.fill((*BLUE, 255))
        pg.draw.rect(self.image, BLACK, self.image.get_rect(), 1)
        text = self.font.render(str(self.lvl), True, BLACK)
        text_size = text.get_size()
        coords = tuple([(a-b)//2 for a, b in zip(self.rect.size, text_size)])
        self.image.blit(text, coords)
        return self.image, self.rect.topleft

    def update(self, ms):
        if self.timer >= self.delay:
            self.timer = 0
        elif self.timer != 0:
            self.timer += ms

        if self.timer == 0:
            for enemy in self.entities['enemies']:
                if enemy.damage <= enemy.health_max:
                    coords = tuple(map(sum, zip(self.rect.center, self.field_coords)))
                    bullet = Bullet(enemy, coords, self.dmg)
                    enemy.damage += bullet.dmg
                    self.entities['bullets'].add(bullet)
                    self.timer += ms
                    break

class Bullet(pg.sprite.Sprite):
    def __init__(self, target, pos, dmg):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((8, 8)).convert_alpha()
        self.image.fill((*RED, 255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.target = target
        self.speed = 12
        self.dmg = dmg

    def update(self, ms):
        # if self.rect.center == self.target.rect.center:
        #     self.target.health -= self.dmg
        #     self.kill()

        vector = tuple([b - a for a, b in zip(self.rect.center, self.target.rect.center)])
        vector = scale_vector(vector, self.speed)
        new_pos = tuple(map(sum, zip(self.rect.center, vector)))

        if all([abs(a - b) < self.speed for a, b in zip(self.target.rect.center, new_pos)]):
            # new_pos = self.target.rect.center
            self.target.health -= self.dmg
            self.kill()
        if not self.target.alive(): # почему то работает и без этого условия
            self.kill()

        self.rect.center = new_pos


