import time

from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN

from random import randrange



class FlyingGame:
    TOP = 10
    BOTTOM = 0
    def __init__(self):
        self.height = 5

    def find_position(self):
        if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
            self.height += 1
        if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
            self.height -= 1
        self.height = min(self.TOP, max(self.BOTTOM, self.height))

    def show_height(self):
        for y in range(11):
            if y == self.height:
                graphics.set_pen(WHITE_PEN)
            else:
                graphics.set_pen(BLACK_PEN)
            graphics.pixel(0, y)
        gu.update(graphics)


gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY_GALACTIC_UNICORN)
WHITE_PEN = graphics.create_pen(255, 255, 255)
BLACK_PEN = graphics.create_pen(0, 0, 0)
fg = FlyingGame()

while True:
    fg.find_position()
    fg.show_height()
    time.sleep(0.1)



