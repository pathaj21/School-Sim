import pygame
from pygame import *
from Character import Character
from Block import Block

""""""
class Spikes(object):
    def __init__(self, color, x1, y1, x2, y2, x3, y3, screen):
        self.color = color
        self.screen = screen
        self.x1 = x1
        self.y1 = y1
        self.firstPoint = x1, x2
        self.x2 = x2
        self.y2 = y2
        self.secondPoint = x2, y2
        self.x3 = x3
        self.y3 = y3
        self.thirdPoint = x3, y3
        self.points = (self.firstPoint, self.secondPoint, self.thirdPoint)

    def update(self):
        oneSpike = draw.polygon(self.screen, self.color, self.points, 0)
