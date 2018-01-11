# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
import sys
from Character import Character

'''Main - Controls Base Game'''
#Currently mostly pseudocode until Player class is finished #

'''Start Pygame'''
pygame.init()

'''Global Variables'''
inGame = True
clock = pygame.time.Clock()
#Window Size
winSize = winHeight, winWidth, = 300, 200
screen = pygame.display.set_mode(winSize)
#Colors
white = 255, 255, 255
black = 0, 0, 0
lightBlue = 230, 230, 250
red = 255, 0, 0
#Objects
#Pseudocode - Player object (X coord, Y coord, Height, Width)
player = Character(red,10,10,100,50,screen)

while inGame:
    '''Event Handler'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #Pseudocode
    if player.left:
        player.x -= player.speed
    if player.right:
        player.x += player.speed
    if player.up:
        player.y += player.speed
    #if not player.isOnGround:
    player.y = 5
    '''Draw'''
    screen.fill(lightBlue)
    player.screenDraw()
    pygame.display.flip()
    xd = 1000//60
    pygame.time.wait(xd)
    clock.tick()
