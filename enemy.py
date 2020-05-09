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
		for i in range(len(self.dots) - 1):
			pg.draw.line(self.image, BLACK, self.dots[i], self.dots[i+1], self.thickness)

	def draw(self):
		return self.image, self.rect.topleft

	def real_dot(self, dot):
		return tuple(map(sum, zip(self.rect.topleft, self.dots[dot])))


class Enemy(pg.sprite.Sprite):
	def __init__(self, rout):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((SCALE//2, SCALE//2)).convert_alpha()
		self.image.fill((*GREEN, 128))
		self.rect = self.image.get_rect()
		self.rout = rout
		self.step = 0
		self.rect.center = self.rout.real_dot(self.step)
		self.speed = 2

	def update(self, ms):
		dest = self.rout.real_dot(self.step + 1)
		vector = tuple([b - a for a, b in zip(self.rect.center, dest)])
		print(f'{self.rect.center=}, {dest=}')
		print(f'{vector=}')
		vector = scale_vector(vector, self.speed)
		new_pos = tuple(map(sum, zip(self.rect.center, vector)))
		
		if all([abs(a - b) < self.speed for a, b in zip(dest, new_pos)]):
			print(dest, new_pos)
			new_pos = dest
			self.step += 1

		self.rect.center = new_pos
		if self.step == len(self.rout.dots) - 1:
			self.kill()