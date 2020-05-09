import pygame as pg
from pygame.locals import *
import random as r
from os import environ

from field import *
from config import *
from enemy import *

class Game:
    def __init__(self):
        pg.init()
        environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % WIN_COORDS
        self.window = pg.display.set_mode(WINSIZE)
        self.bg = load_image(BG, WINSIZE, False, True)
        self.clock = pg.time.Clock()
        self.running = False
        self.scheme_exists = False
        self.entities = {
            'enemies': pg.sprite.Group(),
            'bullets': pg.sprite.Group(),
        }
        self.field = Field(self.window, self.entities)
        self.rout = Rout(self.field)
        self.enemies_count = 0
        self.enemy_hp = 10

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
                if e.key == K_SPACE:
                    self.field.new_tower()
                if e.key == K_s:
                    enemy = Enemy(self.rout, self.enemy_hp)
                    enemy.add(self.entities['enemies'])
                    self.enemies_count += 1
                    if self.enemies_count > 10:
                        self.enemy_hp = int(self.enemy_hp * 1.1)
                        self.enemies_count -= 10

    def update(self):
        ms = self.clock.tick_busy_loop(FPS)
        self.entities['enemies'].update(ms)
        self.entities['bullets'].update(ms)
        self.field.update(ms)

    def draw_scheme(self):
        '''
        function for placement planning
        '''
        if not self.scheme_exists:
            self.scheme = pg.Surface(self.window.get_size()).convert_alpha()
            self.scheme.fill((*WHITE, 64))
            # self.scheme.set_alpha(128)
            self.scheme_exists = True
            # интерфейс игры
            # pg.draw.line(self.scheme, BLACK, (W//2, 0), (W//2, H), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*0.4)), (W, int(H*0.4)), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*0.8)), (W, int(H*0.8)), 1)
            # поля
            # pg.draw.line(self.scheme, BLACK, (int(W*2/9), 0), (int(W*2/9), H), 1)
            # pg.draw.line(self.scheme, BLACK, (int(W*7/9), 0), (int(W*7/9), H), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*3/16)), (W, int(H*3/16)), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*6/16)), (W, int(H*6/16)), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*8/16)), (W, int(H*8/16)), 1)
            # pg.draw.line(self.scheme, BLACK, (0, int(H*11/16)), (W, int(H*11/16)), 1)
                        
        self.window.blit(self.scheme, (0, 0))

    def render(self):
        self.window.blit(self.bg, (0, 0))
        pg.display.set_caption(f'FPS: {self.clock.get_fps()}')
        self.draw_scheme()
        self.window.blit(*self.field.draw())
        self.window.blit(*self.rout.draw())
        self.entities['enemies'].draw(self.window)
        self.entities['bullets'].draw(self.window)
        pg.display.update()

if __name__ == '__main__':
    Game().run()