# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import random
import sys
import pygame as pg
from typing import TypeVar, List, Callable, Dict

T = TypeVar("T")


class Ball(object):
    def __init__(self):
        self.posX = 0
        self.posY = 0
        self.velX = 0
        self.velY = 0
        self.radiMass = 0

    def get_location(self):
        return self.posX, self.posY

    def set_location(self, x, y):
        self.posX = x
        self.posY = y
        return

    def get_velocity(self):
        return self.velX, self.velY

    def set_velocity(self, v_x, v_y):
        self.velX = v_x
        self.velY = v_y
        return

    def update_position(self):
        self.posX += self.velX
        self.posY += self.velY
        return

    def set_radiMass(self, newRadiMass):
        self.radiMass = newRadiMass
        return

    def gravity(self, x, y):
        return self.radiMass / ((math.sqrt((self.posX - x) ** 2 + (self.posY - y) ** 2) + 0.001)**2)


def main():
    pg.init()
    clock = pg.time.Clock()

    screen = pg.display.set_mode([504, 504])

    # stops at chunk 19 for 20fps
    # screen = pg.display.set_mode([1920, 1080])

    screen.fill([230, 230, 230])

    c1 = Ball()
    c1.set_location(100, 200)
    c1.set_radiMass(50)
    c1.set_velocity(1, .8)

    c2 = Ball()
    c2.set_location(250, 180)
    c2.set_radiMass(70)
    c2.set_velocity(-1, -.1)

    c3 = Ball()
    c3.set_location(400, 400)
    c3.set_radiMass(30)
    c3.set_velocity(1.5, -1)

    c4 = Ball()
    c4.set_location(500, 500)
    c4.set_radiMass(50)
    c4.set_velocity(-1, -1)

    c5 = Ball()
    c5.set_location(0, 500)
    c5.set_radiMass(25)
    c5.set_velocity(.5, -1)

    # x, y, radius, xvel, yvel
    # c2 = [250, 200, 100, 0, 0]
    # c3 = [300, 200, 100, -.5, -.4]

    Ball_list = []

    Ball_list.append(c1)
    Ball_list.append(c2)
    Ball_list.append(c3)
    Ball_list.append(c4)
    Ball_list.append(c5)

    chunk = 1
    frame = 0
    while True:
        frame += 1
        # weird and bad fps scaling code
        # if frame % 20 == 0:
        #     fps = clock.get_fps()
        #     print("Chunk:", chunk, " FPS:", fps)
        #     if fps < 20:
        #         chunk += 2


        clock.tick(100)
        screen.fill([200, 200, 230])

        for ball in Ball_list:
            ball.update_position()

            if ball.velX < 0 and ball.posX - ball.radiMass < 0:
                ball.velX *= -1
            elif ball.velX > 0 and ball.posX + ball.radiMass > screen.get_width():
                ball.velX *= -1

            if ball.velY < 0 and ball.posY - ball.radiMass < 0:
                ball.velY *= -1
            elif ball.velY > 0 and ball.posY + ball.radiMass > screen.get_height():
                ball.velY *= -1


            # pg.draw.circle(screen, [190, 190, 190], (ball.get_location()), ball.radiMass)
        for y in range(math.floor(screen.get_height() / chunk)):
            for x in range(math.floor(screen.get_width() / chunk)):
                sum_gravity = 0
                for ball in Ball_list:
                    sum_gravity += ball.gravity(x*chunk + chunk/2, y*chunk + chunk/2) * ball.radiMass
                if sum_gravity > 1.0:
                    #color1 = [100 + math.floor(sum_gravity**2), 100 + math.floor(sum_gravity**3), 100 + math.floor(sum_gravity)]
                    color1 = [100 + math.floor(sum_gravity ** 2), 100 + math.floor(sum_gravity), 100 + math.floor(sum_gravity)]
                    for i in range(len(color1)):
                        if color1[i] > 255:
                            color1[i] = 255

                    # for i in range(chunk):
                    #     for j in range(chunk):
                    #         screen.set_at((x * chunk + i, y * chunk + j), color1)
                    pg.draw.rect(screen, color1, (x * chunk, y * chunk, chunk, chunk))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        pg.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
