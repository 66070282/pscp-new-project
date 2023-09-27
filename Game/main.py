import pygame as pg
import constants as c

#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("การเอาคืนของป้อม DEMO")

#new icon
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)

#game loop
run = True
while run:

    clock.tick(c.FPS)

    #event control
    for event in pg.event.get():
        #exit game
        if event.type == pg.QUIT:
            run = False

pg.quit()