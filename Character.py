""" Project - Platformer
 Patrick Hajdukiewicz
 Aidan Parkhurst
 Nadil Ranatunga
 Jake Valencia
 stuff."""

import pygame
from pygame import *


class Character(sprite.Sprite):
    def __init__(self, color, x, y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.left = False
        self.right = False
        self.up = False

    def moveRight(self):
        self.right = True

    def moveLeft(self):
        self.left = True

    def moveUp(self):
        self.up = True

    def keyPressing(self):
        key.get_focused()

