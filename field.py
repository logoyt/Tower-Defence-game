import pygame as pg
import random as r

from tower import *
from config import *

class Field():
	def __init__(self, window, entities, pos=(W//2, H//2)):
		self.field = [[None] * 5 for _ in range(3)]
		self.cell = SCALE
		self.gap = max(2, self.cell // 12)
		w = self.cell * len(self.field[0]) + self.gap * (len(self.field[0]) + 4 - 1)
		h = self.cell * len(self.field)    + self.gap * (len(self.field)    + 4 - 1)
		self.image = pg.Surface((w, h)).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = pos

		self.entities = entities

	def update(self, ms):
		self.image.fill((*WHITE, 128))
		# рисуем рамку и клетки
		pg.draw.rect(self.image, BLACK, self.image.get_rect(), 1)
		for col in range(len(self.field[0])):
			x = self.gap + (self.gap + self.cell) * (col + 1) - self.cell
			for row in range(len(self.field)):
				y = self.gap + (self.gap + self.cell) * (row + 1) - self.cell
				if self.field[row][col] is None:
					pg.draw.rect(self.image, BLACK, (x, y, self.cell, self.cell), 1)
				else:
					self.field[row][col].update(ms)
					self.image.blit(*self.field[row][col].draw())

	def draw(self):
		return self.image, self.rect.topleft

	def new_tower(self):
		if any([None in line for line in self.field]):
			while True:
				row = r.randint(0, len(self.field)    - 1)
				col = r.randint(0, len(self.field[0]) - 1)
				if self.field[row][col] is None:
					x = self.gap + (self.gap + self.cell) * (col + 1) - self.cell
					y = self.gap + (self.gap + self.cell) * (row + 1) - self.cell
					self.field[row][col] = Tower((x, y), self.entities, self.rect.topleft)
					break

