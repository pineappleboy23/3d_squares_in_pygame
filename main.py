import pygame as pg
import random
import math
import time

pg.init()

clock = pg.time.Clock()

sw = 1400
sh = 700
screen_color = (48, 141, 240)

pg.display.set_caption("3D")
win = pg.display.set_mode((sw, sh))
win.fill(screen_color)


class Box(object):
    def __init__(self):
        self.color = (50, 50, 150)


class Side(object):
    def __init__(self):
        self.corner1_3d = (100, 100, 0)
        self.corner1_2d = (100, 100)


class FourSide(object):
    def __init__(self):
        self.color = (50, 200, 150)
        self.corner1_3d = (500, 500, 0)
        self.corner1_2d = (500, 500)

        self.corner2_3d = (600, 500, 0)
        self.corner2_2d = (600, 500)

        self.corner3_3d = (600, 600, 0)
        self.corner3_2d = (600, 600)

        self.corner3_3d = (500, 600, 0)
        self.corner4_2d = (500, 600)


    def get_2d_cords(self):
        pass


    def draw(self, win):

        pg.draw.polygon(win, self.color, [self.corner1_2d, self.corner2_2d, self.corner3_2d, self.corner4_2d])


class Square(object):
    def __init__(self):
        self.color = (120, 120, 120)

        self.ri = False
        self.le = False
        self.up = False
        self.do = False
        self.shrink = False

        self.speed = 3

        self.x = 700
        self.y = 200
        self.z = 0
        self.side = 300

        self.center = (self.x + self.side/2, self.y + self.side/2)

        self.display_x = self.x
        self.display_y = self.y

        self.scale = 1.0
        self.original_angle = (self.side/sh) * 180
        self.perceived_angle = self.original_angle
        self.perceived_side = self.scale * self.side



    def get_2d_cords(self):
        self.get_scale_from_z_value()

        self.center = (self.x + self.side/2, self.y + self.side/2)

        self.display_x = self.center[0] - self.perceived_side/2
        self.display_y = self.center[1] - self.perceived_side/2


    def get_scale_from_z_value(self):
        if self.z == 0:
            self.perceived_angle = 180
        else:
            self.perceived_angle = (2 * 180 * math.atan((self.side/2) / self.z)) / math.pi

        self.scale = (self.perceived_angle / 180)

        self.perceived_side = self.scale * self.side


    def move(self):
        if self.ri:
             self.x += self.speed * self.scale
        if self.le:
            self.x -= self.speed * self.scale
        if self.up:
            self.y -= self.speed * self.scale
        if self.do:
              self.y += self.speed * self.scale
        if self.shrink:
              self.z += self.speed * self.scale


    def draw(self, win):
        self.get_2d_cords()
        pg.draw.rect(win, self.color, (self.display_x, self.display_y, self.perceived_side, self.perceived_side))


def redraw_game_window():
    win.fill(screen_color)

    square.draw(win)

    for i in all_my_squares:
        i.draw(win)

    pg.display.update()


square = Square()

all_my_squares = []
for i in range(11):
    temp = Square()
    temp.x = random.choice(range(sw - 200))
    temp.y = random.choice(range(sh - 200))
    temp.z = random.choice(range(200))  # 200 is arbitrary
    new_color = (random.choice(range(255)), random.choice(range(255)), random.choice(range(255)))

    temp.color = new_color


    all_my_squares.append(temp)



running = True
while running:

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT or event.key == ord('a'):
                square.le = True
                for i in all_my_squares:
                    i.le = True
            if event.key == pg.K_RIGHT or event.key == ord('d'):
                square.ri = True
                for i in all_my_squares:
                    i.ri = True
            if event.key == pg.K_UP or event.key == ord('w'):
                square.up = True
                for i in all_my_squares:
                    i.up = True
            if event.key == pg.K_DOWN or event.key == ord('s'):
                square.do = True
                for i in all_my_squares:
                    i.do = True

            if event.key == ord('b'):
                square.shrink = True
                for i in all_my_squares:
                    i.shrink = True


        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == ord('a'):
                square.le = False
                for i in all_my_squares:
                    i.le = False
            if event.key == pg.K_RIGHT or event.key == ord('d'):
                square.ri = False
                for i in all_my_squares:
                    i.ri = False
            if event.key == pg.K_UP or event.key == ord('w'):
                square.up = False
                for i in all_my_squares:
                    i.up = False
            if event.key == pg.K_DOWN or event.key == ord('s'):
                square.do = False
                for i in all_my_squares:
                    i.do = False

            if event.key == ord('b'):
                square.shrink = False
                for i in all_my_squares:
                    i.shrink = False


    square.move()

    for i in all_my_squares:
        i.move()


    redraw_game_window()
