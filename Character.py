""" Project - Platformer
 Patrick Hajdukiewicz
 Aidan Parkhurst
 Nadil Ranatunga
 Jake Valencia
 stuff."""

from pygame import *


class Character(sprite.Sprite):
    def __init__(self, color, height, width, x, y, left, right, up):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.left = left
        self.right = right
        self.up = up

    def moveRight(self):
        self.x += 1
        self.right = True

    def moveLeft(self):
        self.x -= 1
        self.left = True

    def moveUp(self):
        self.y += 8
        self.up = True

    def keyPressing(self):
        key.get_focused()

