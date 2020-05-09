import pygame as pg

from config import *

class Rout():
	def __init__(self, field):
		w, h = field.rect.size
		w += 2 * SCALE
		h += 2 * SCALE
		x, y = field.rect.topleft
		self.rect = pg.Rect(x - SCALE, y - SCALE, w, h)
		self.image = pg.Surface((w, h)).convert_alpha()
		self.image.fill((*WHITE, 0))
		self.dots = [
			(SCALE//2,     h - SCALE//2),
			(SCALE//2,     SCALE//2    ),
			(w - SCALE//2, SCALE//2    ),
			(w - SCALE//2, h - SCALE//2),
		]
		self.thickness = 3
		print(self.dots)
		for i in range(len(self.dots) - 1):
			pg.draw.line(self.image, BLACK, self.dots[i], self.dots[i+1], self.thickness)

	def draw(self):
		return self.image, self.rect.topleft


class Enemy():
	def __init__(self, pos):
		self.image = pg.Surface((SCALE, SCALE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.topleft = pos

	def draw(self):
		return self.image, self.rect.topleft