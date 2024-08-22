import pygame as pg
from random import randrange
from mainloop import graj

pg.init()

window = 1000
tile_size = 50
points = 0

screen = pg.display.set_mode((window, window))
pg.display.set_caption('Szymon Baca 101940')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = True
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                points = graj(points)
    
    pg.display.flip()
