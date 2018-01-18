# Project - Platformer
# Patrick Hajdukiewicz
# Aidan Parkhurst
# Nadil Ranatunga
# Jake Valencia

import pygame
import sys
import os
import pygame
from Character import Character
from Block import Block
from Level import Level
from Spike import Spikes

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
os.environ['SDL_VIDEO_CENTERED'] = '1'
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
spikeGroup = pygame.sprite.Group()
player = Character(red, 10, 10, 50, 25, defaultFallSpeed, 16, screen)
groundBlock1 = Block(lightGray, 0, winHeight - 25, 25, 300, screen)
groundBlock2 = Block(lightGray, 550, winHeight - 25, 25, 300, screen)
playerGroup.add(player)
groundBlocks.add(groundBlock1,groundBlock2)
level1 = Level(groundBlocks,spikeGroup)
levelList.append(level1)

spikeGroup2 = pygame.sprite.Group()
spike1 = Spikes(black, 100, winHeight - 25, 125, winHeight - 100, 150,winHeight - 25, screen)
groundBlocks2 = pygame.sprite.Group()
groundBlock3 = Block(lightGray, 0, winHeight - 25, 25, 800, screen)
groundBlocks2.add(groundBlock3)
spikeGroup2.add(spike1)
level2 = Level(groundBlocks2,spikeGroup2)
levelList.append(level2)

spikeGroup3 = pygame.sprite.Group()
spike2 = Spikes(black, 150, winHeight - 25, 175, winHeight - 100, 200,winHeight - 25, screen)
groundBlocks3 = pygame.sprite.Group()
groundBlock4 = Block(lightGray, 0, winHeight - 25, 25, 800, screen)
groundBlocks3.add(groundBlock3)
spikeGroup3.add(spike2)
level3 = Level(groundBlocks3,spikeGroup3)
levelList.append(level3)

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
            if curLev % 2 == 1 and curLev < (len(levelList) - 1):
                curLev += 1
                player.curSpawnX = 10
                player.curSpawnY = 100
    if player.right:
        if not player.limitRight:
            player.x += player.defaultPlayerSpeed
        else:
            player.x -= 2
            player.limitRight = False
        if player.x >= winWidth - player.width:
            player.x = winWidth - player.width
            if curLev % 2 == 0 and curLev < (len(levelList) - 1):
                curLev += 1
                player.curSpawnX = winWidth - 10 - player.width
                player.curSpawnY = 100
    if player.up and not player.jumping:
        player.y -= player.jumpHeight + player.jumpTimer
        if player.jumpTimer <= 0:
            player.jumping = True
            player.jumpTimer = defaultJumpTimer
        else:
            player.jumpTimer -= 1
    if player.down:
        player.y += player.fallSpeed
        if player.y + player.height >= winHeight:
            player.die(player.curSpawnX,player.curSpawnY)
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
    for spike in loadLevel.spikes:
        if player.spikeHit(spike):
            player.jumpTimer = 0
            player.down = True
            player.fallSpeed = defaultFallSpeed
    '''Draw'''
    screen.fill(lightBlue)
    loadLevel.update()
    playerGroup.update()
    pygame.display.flip()
    xd = 1000//60
    pygame.time.wait(xd)
    clock.tick()