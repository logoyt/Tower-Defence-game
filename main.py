import pygame as pg
from pygame.locals import *
import random as r
from os import environ

from config import *

class Game:
	def __init__(self):
		pg.init()
		environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % WIN_COORDS
		self.window = pg.display.set_mode(WINSIZE)
		self.bg = load_image(BG, WINSIZE, False, True)
		self.clock = pg.time.Clock()
		self.running = False

	def run(self):
		self.running = True
		while self.running:
			self.events()
			self.update()
			self.render()

	def events(self):
		for e in pg.event.get():
			if e.type == QUIT:
				self.running = False
				return
			if e.type == KEYUP:
				if e.key == K_ESCAPE:
					self.running = False
					return

	def update(self):
		ms = self.clock.tick_busy_loop(FPS)

	def render(self):
		self.window.blit(self.bg, (0, 0))
		pg.display.set_caption(f'FPS: {self.clock.get_fps()}')

		pg.display.update()

if __name__ == '__main__':
	Game().run()