import pygame as pg
from config import *

class Field(pg.sprite.Sprite):
	def __init__(self, window, pos=(W//2, H//2)):
		self.field = [[None] * 5 for _ in range(3)]
		self.cell = SCALE
		self.gap = max(2, self.cell // 12)
		w = self.cell * len(self.field[0]) + self.gap * (len(self.field[0]) + 4 - 1)
		h = self.cell * len(self.field)    + self.gap * (len(self.field)    + 4 - 1)
		self.image = pg.Surface((w, h))
		self.rect = self.image.get_rect()
		self.rect.center = pos

		self.image.set_alpha(128)

	def update(self, ms):
		self.image.fill(WHITE)
		# рисуем рамку и клетки
		pg.draw.rect(self.image, BLACK, self.image.get_rect(), 1)
		for col in range(len(self.field[0])):
			x = self.gap + (self.gap + self.cell) * (col + 1) - self.cell
			for row in range(len(self.field)):
				y = self.gap + (self.gap + self.cell) * (row + 1) - self.cell
				if self.field[row][col] is None:
					pg.draw.rect(self.image, BLACK, (x, y, self.cell, self.cell), 1)
				else:
					self.image.blit(*self.field[y][x].draw())

	def draw(self):
		return self.image, self.rect.topleft



# if __name__ == '__main__':
# 	Field()
