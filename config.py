import os
import pygame as pg
from math import ceil, sqrt
from tkinter import Tk

def load_image(img, rez, alpha=True, crop=False):
	img = pg.image.load(img)
	if crop:
		w, h = img.get_size()
		# увеличиваем изначальную картинку, если по одной из сторон она меньше
		if rez[0] > w or rez[1] > h:
			scale = max(rez[0] / w, rez[1] / h)
			img = pg.transform.scale(img, (ceil(w * scale), ceil(h * scale)))
			w, h = img.get_size()
		# уменьшаем изначальную картинку, если по обеим сторонам она больше
		if w > rez[0] and h > rez[1]:
			scale = max(rez[0] / w, rez[1] / h)
			img = pg.transform.scale(img, (ceil(w * scale), ceil(h * scale)))
			w, h = img.get_size()
		# обрезаем излишки
		img = img.subsurface((0, 0, *rez))

	img = pg.transform.scale(img, rez)
	if alpha:
		img.convert_alpha()
	else:
		img.convert()
	return img

def scale_vector(vector, length):
	l = sqrt(sum([i**2 for i in vector]))
	scale = length / l
	return tuple([i * scale for i in vector])

temp = Tk()
SCREEN = temp.winfo_screenwidth(), temp.winfo_screenheight()
del temp

SCALE = 48
WINSIZE = W, H = 9 * SCALE, 16 * SCALE
FPS = 60

# WIN_COORDS = (SCREEN[0] - W) // 2, (SCREEN[1] - H) // 2
WIN_COORDS = (SCREEN[0] - W - 100, 100)
# print(WINSIZE)

current_dir = os.path.dirname(__file__)
textures = os.path.join(current_dir, 'textures')
BG = os.path.join(textures, 'bg.jpg')

# COLORS   R    G    B    T
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BLUE  = (173, 188, 230)
GREEN = (188, 230, 173)