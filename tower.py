import pygame as pg

from config import *

class Tower():
	def __init__(self, pos):
		self.image = pg.Surface((SCALE, SCALE)).convert()
		self.image.fill(BLUE)

		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	def draw(self):
		return self.image, self.rect.topleft
