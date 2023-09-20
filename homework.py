import math
import time
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(0, 90)

x = 0
y = 90
angle = 0
radius = 100
center_x, center_y = 400, 300

while (1):
    
    while (x < 800) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)
    while (y < 570) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(790, y)
        y = y + 2
        delay(0.01)
    while (10 < x) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 570)
        x = x - 2
        delay(0.01)
    while (90 < y) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y = y - 2
        delay(0.01)
    x = center_x + radius
    y = center_y
    while (angle < 361) :
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        angle += 1
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        delay(0.01)

close_canvas()
    
