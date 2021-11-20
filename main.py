import pygame as pg
import random as rd
import math
import sys

from pygame.time import Clock

pg.init()

screen = pg.display.set_mode((500,500))
title = pg.display.set_caption("TEST")

#REDRAWING SCREEN
def redraw():
    screen.fill((0,0,0))
    pg.display.update()

#FOOD
def food():
    food_x = 200
    food_y = 200
    FOOD_COLOR = (255,255,255,0)
    FWIDTH = 15
    fooddraw = pg.draw.circle(screen, FOOD_COLOR, (food_x, food_y), FWIDTH)

#ANT VARIABLES
ant_x = 200
ant_y = 200
COLOR = (220,20,60,0)
ANT_WIDTH = 5

#RANDOM MOVES USING VECTOR
def move(ants):
    ant_x, ant_y = ants
    x_boundary = 1000
    y_boundary = 1000
    pos = pg.math.Vector2(ant_x, ant_y)
    ant_x = rd.randrange(0, x_boundary)
    ant_y = rd.randrange(0, y_boundary)
    speed = 1
    maxdist = 1
    dist = rd.randrange(maxdist)
    direction = pg.math.Vector2(1, 2).rotate(rd.randrange(360))

    pos += direction * speed
    dist -= speed
    ant_x, ant_y = round(pos.x), round(pos.y)

    if dist <= 0:
        dist = rd.randrange(maxdist)
        direction = pg.math.Vector2(1, 0).rotate(rd.randrange(360))
    else:
        pass
    if ant_x >= screen.get_width(): #IF ANTS X IS OFF THE SCREEN WIDTH THEN RESET THE X POSITION
        ant_x = 200
        dist = rd.randrange(maxdist)
        direction = pg.math.Vector2(1, 0).rotate(rd.randrange(360))
    else:
        pass
    if ant_y >= screen.get_height(): #RESET POSITION IF ANTS Y IS OFF THE SCREEN HEIGHT
        ant_x = 200
        dist = rd.randrange(maxdist)
        direction = pg.math.Vector2(1, 0).rotate(rd.randrange(360))
    else:
        pass
    ants[0] = ant_x
    ants[1] = ant_y

#TRIED TO DUPLICATE ANT WITH DIFFERENT MOVES
ant_spawn = []
for i in range(70):
    for j in range(2):
        ant_x = 250
        ant_y = 250
        ant_spawn.append([ant_x, ant_y])

alpha_surf = pg.draw.circle(screen, (255,255,255,0), (ant_x, ant_y), 3)
trail_list = []
    
while True:
    FPS = pg.time.Clock()
    redraw()
    pg.display.flip()
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            pg.quit()
    #APPEND TO SCREEN
    for ants in ant_spawn:
        pg.draw.rect(screen, COLOR, (*ants, 3, 3))

    for ants in ant_spawn:
        move(ants)


    pg.display.update()
    FPS.tick(60)