# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
import sys

'''Main - Controls Base Game'''
#Currently mostly pseudocode until Player class is finished #

'''Start Pygame'''
pygame.init()

'''Global Variables'''
inGame = True
#Window Size
winSize = winHeight, winWidth, = 300, 200
screen = pygame.display.set_mode(winSize)
#Colors
white = 255, 255, 255
black = 0, 0, 0
lightBlue = 230, 230, 250
#Objects
#Pseudocode - Player object (X coord, Y coord, Height, Width)
player = character(10,10,100,50)

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
    if not player.isOnGround:
        player.y -= 5

    '''Draw'''
    screen.fill(lightBlue)
    pygame.display.flip()
