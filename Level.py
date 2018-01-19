# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

from pygame import *
import pygame

class Level(object):

    def __init__(self,blockGroup : pygame.sprite.Group, spikeGroup : pygame.sprite.Group, spawnX, spawnY):
        self.blocks = blockGroup
        self.spikes = spikeGroup
        self.spawnX = spawnX
        self.spawnY = spawnY

    def update(self):
        self.blocks.update()
        self.spikes.update()