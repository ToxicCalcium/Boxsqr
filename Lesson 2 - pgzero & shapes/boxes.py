import pgzrun
import random

WIDTH=300
HEIGHT=300

def draw():
    width = WIDTH
    height = HEIGHT - 300
    red1 = 255
    green1 = 0
    blue1 = random.randint(120, 255)
    for i in range(40):
        r = Rect((0, 0), (width, height))
        r.center = (150, 150)
        screen.draw.rect(r, (red1, green1, blue1))
        width -= 10
        height += 10
        red1 -= 10
        green1 += 10

pgzrun.go()