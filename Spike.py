import pygame
from pygame import *
from Character import Character
from Block import Block

""""""
class Spikes(sprite.Sprite):
    def __init__(self, color, x1, y1, x2, y2, x3, y3, screen):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.firstPoint = [x1, y1]
        self.x2 = x2
        self.y2 = y2
        self.secondPoint = [x2, y2]
        self.x3 = x3
        self.y3 = y3
        self.thirdPoint = [x3, y3]
        self.points = (self.firstPoint, self.secondPoint, self.thirdPoint)

    def update(self):
        oneSpike = draw.polygon(self.screen, self.color, self.points, 0)

    def getArea(self,x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def contains(self,x,y):
        A = self.getArea(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)
        #Triangle PBC
        A1 = self.getArea(x, y, self.x2, self.y2, self.x3, self.y3)
        #Triangle PAC
        A2 = self.getArea(self.x1, self.y1, x, y, self.x3, self.y3)
        #Triangle PAB
        A3 = self.getArea(self.x1, self.y1, self.x2, self.y2, x, y)
        if (A == A1 + A2 + A3):
            return True
        else:
            return False