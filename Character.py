""" Project - Platformer
 Patrick Hajdukiewicz
 Aidan Parkhurst
 Nadil Ranatunga
 Jake Valencia
 stuff."""

import pygame
from pygame import *

class Character(sprite.Sprite):
    def __init__(self, color, x, y, height, width, fallSpeed, maxFallSpeed, screen):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.curSpawnX = 10
        self.curSpawnY = 100
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.down = False
        self.left = False
        self.right = False
        self.up = False
        self.jumping = True
        self.jumpTimer = 20
        self.fallSpeed = fallSpeed
        self.maxFallSpeed = maxFallSpeed
        self.screen = screen
        self.defaultPlayerSpeed = 8
        self.jumpHeight = 10
        self.limitLeft = False
        self.limitRight = False

    def moveRight(self):
        self.right = True

    def moveLeft(self):
        self.left = True

    def moveUp(self):
        self.up = True

    def fall(self):
        self.y -= self.fallSpeed

    def onGround(self,block):
        if block.contains(self.x,self.y + .5*self.height) or block.contains(self.x + self.width, self.y + .5*self.height):
           return False
        if self.x + self.width > block.x and self.x <= block.x + block.width:
            if self.y + self.height >= block.y and self.y + self.height <= block.y + block.height:
                self.y -= (self.y + self.height) - (block.y)
                return True
            return False
        return False

    def headHit(self,block):
        if block.contains(self.x,self.y + .5*self.height) or block.contains(self.x + self.width, self.y + .5*self.height):
           return False
        if self.x + self.width > block.x and self.x <= block.x + block.width:
            if self.y >= block.y and self.y <= block.y + block.height:
                self.y += (block.y + block.height) - self.y
                return True
            return False
        return False

    def rightHit(self,block):
        if block.contains(self.x + self.width, self.y + .5* self.height) \
                and (block.contains(self.x + self.width, self.y) or block.contains(self.x + self.width, self.y + self.height)):
            return True
        else:
            return False

    def leftHit(self,block):
        if block.contains(self.x, self.y + .5* self.height) \
                and (block.contains(self.x,self.y) or block.contains(self.x, self.y + self.height)):
            return True
        else:
            return False

    def spikeHit(self,spike):
        if spike.contains(self.x + self.width, self.y + .5* self.height)\
                or spike.contains(self.x, self.y + .5* self.height)\
                or spike.contains(self.x,self.y)\
                or spike.contains(self.x, self.y + self.height)\
                or spike.contains(self.x + self.width,self.y)\
                or spike.contains(self.x + self.width, self.y + self.height):
            self.die(self.curSpawnX,self.curSpawnY)
            return True
        return False

    def die(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen,self.color,rectangle,0)

