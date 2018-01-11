# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
import sys
from Character import Character
from Block import Block

'''Main - Controls Base Game'''
'''Start Pygame'''
pygame.init()

'''Global Variables'''
#Misc
defaultFallSpeed = 3
inGame = True
clock = pygame.time.Clock()
#Window Size
winSize = winHeight, winWidth, = 800, 600
screen = pygame.display.set_mode(winSize)
pygame.display.set_caption("School Platformer!")
#Colors
white = 255, 255, 255
black = 0, 0, 0
lightBlue = 230, 230, 250
red = 255, 0, 0
lightGray = 169, 169, 169
#Objects
playerGroup = pygame.sprite.Group()
groundBlocks = pygame.sprite.Group()
player = Character(red, 10, 10, 100, 50, defaultFallSpeed, 10, screen)
groundBlock = Block(lightGray, 0, winHeight - 225, 25, 800, screen)
playerGroup.add(player)
groundBlocks.add(groundBlock)

while inGame:
    '''Event Handler'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if player.left:
        player.x -= player.speed
    if player.right:
        player.x += player.speed
    if player.up:
        player.y += player.speed
    for block in groundBlocks:
        if player.y + player.height >= block.y:
            player.y -= player.fallSpeed
            player.fallSpeed = defaultFallSpeed
        else:
            if player.fallSpeed <= player.maxFallSpeed:
                player.fallSpeed += 1
    player.y += player.fallSpeed
    '''Draw'''
    screen.fill(lightBlue)
    groundBlocks.update()
    playerGroup.update()
    pygame.display.flip()
    xd = 1000//60
    pygame.time.wait(xd)
    clock.tick()
