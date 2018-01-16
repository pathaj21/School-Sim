# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
import sys
from Character import Character
from Block import Block
from Level import Level

'''Main - Controls Base Game'''
'''Start Pygame'''
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Resources/8BitGR.ogg")
pygame.mixer.music.play(loops=-1, start=0.0)
pygame.mixer.music.set_volume(0.2)

'''Global Variables'''
#Misc
defaultFallSpeed = 8
defaultJumpTimer = 22
inGame = True
clock = pygame.time.Clock()
levelList = []
curLev = 0

#Window Size
winSize = winWidth, winHeight, = 800, 600
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
player = Character(red, 10, 10, 50, 25, defaultFallSpeed, 16, screen)
groundBlock1 = Block(lightGray, 0, winHeight - 25, 25, 300, screen)
groundBlock2 = Block(lightGray, 550, winHeight - 25, 25, 300, screen)
playerGroup.add(player)
groundBlocks.add(groundBlock1,groundBlock2)
level1 = Level(groundBlocks)
levelList.append(level1)

groundBlocks2 = pygame.sprite.Group()
groundBlock3 = Block(lightGray, 0, winHeight - 25, 25, 800, screen)
groundBlocks2.add(groundBlock3)
level2 = Level(groundBlocks2)
levelList.append(level2)

while inGame:
    '''Event Handler'''
    loadLevel = levelList[curLev]
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.left = True
            if event.key == pygame.K_d:
                player.right = True
            if event.key == pygame.K_w:
                player.up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.left = False
            if event.key == pygame.K_d:
                player.right = False
            if event.key == pygame.K_w:
                player.up = False
                player.jumpTimer = 0
                player.fallSpeed = defaultFallSpeed
    if player.left:
        if not player.limitLeft:
            player.x -= player.defaultPlayerSpeed
        else:
            player.x += 2
            player.limitLeft = False
        if player.x <= 0:
            player.x = 0
    if player.right:
        if not player.limitRight:
            player.x += player.defaultPlayerSpeed
        else:
            player.x -= 2
            player.limitRight = False
        if player.x >= winWidth - player.width:
            player.x = winWidth - player.width
    if player.up and not player.jumping:
        player.y -= player.jumpHeight + player.jumpTimer
        if player.jumpTimer <= 0:
            player.jumping = True
            player.jumpTimer = defaultJumpTimer
        else:
            player.jumpTimer -= 1
    if player.down:
        player.y += player.fallSpeed
        if player.fallSpeed < player.maxFallSpeed:
            player.fallSpeed += 1
    for block in loadLevel.blocks:
        if player.leftHit(block):
            player.limitLeft = True
        if player.rightHit(block):
            player.limitRight = True
        if not player.onGround(block):
            player.down = True
        else:
            player.jumping = False
            player.jumpTimer = defaultJumpTimer
            player.fallSpeed = defaultFallSpeed
        if player.headHit(block):
            player.jumpTimer = 0
            player.down = True
            player.fallSpeed = defaultFallSpeed
    '''Draw'''
    screen.fill(lightBlue)
    loadLevel.blocks.update()
    playerGroup.update()
    pygame.display.flip()
    xd = 1000//60
    pygame.time.wait(xd)
    clock.tick()