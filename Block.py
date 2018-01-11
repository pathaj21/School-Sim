# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
from pygame import *

class Block(sprite.Sprite):
    def __init__(self,color,x,y,height,width,screen):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.screen = screen

    def update(self):
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, rectangle, 0)