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
defaultJumpTimer = 15
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
player = Character(red,10,100,50,25,defaultFallSpeed,12,screen)
playerGroup.add(player)

'''Levels'''
#Level 1
lvl1blocks = pygame.sprite.Group()
lvl1spikes = pygame.sprite.Group()
lvl1block1 = Block(lightGray,0,winHeight - 100,100,100,screen)
lvl1block2 = Block(lightGray,200,winHeight-180,100,100,screen)
lvl1block3 = Block(lightGray,400,winHeight-280,100,100,screen)
lvl1block4 = Block(lightGray,600,winHeight-380,100,100,screen)
lvl1blocks.add(lvl1block1,lvl1block2,lvl1block3,lvl1block4)
lvl1 = Level(lvl1blocks,lvl1spikes,10,winHeight - 300)
levelList.append(lvl1)

#Level 2
lvl2blocks = pygame.sprite.Group()
lvl2spikes = pygame.sprite.Group()
lvl2block1 = Block(lightGray,winWidth - 300,winHeight - 50,50,300,screen)
lvl2block2 = Block(lightGray,winWidth - 550,winHeight - 50,50,100,screen)
lvl2block3 = Block(lightGray,0,winHeight - 50,50,50,screen)
lvl2blocks.add(lvl2block1,lvl2block2,lvl2block3)
lvl2spike1 = Spikes(black,winWidth - 200,winHeight - 50,winWidth - 175,winHeight - 125,winWidth - 150,winHeight - 50, screen)
lvl2spikes.add(lvl2spike1)
lvl2 = Level(lvl2blocks,lvl2spikes, winWidth - player.width - 10, winHeight - 200)
levelList.append(lvl2)

#Level 3
lvl3blocks = pygame.sprite.Group()
lvl3spikes = pygame.sprite.Group()
lvl3block1 = Block(lightGray,0,winHeight - 50,60,100,screen)
lvl3block2 = Block(lightGray,200,winHeight - 100,50,90,screen)
lvl3block3 = Block(lightGray,350,winHeight - 500,350,25,screen)
lvl3block4 = Block(lightGray,525,winHeight - 80,50,200,screen)
lvl3block5 = Block(lightGray,winWidth - 25,200,winHeight,25,screen)
lvl3block6 = Block(lightGray,winWidth - 350,175,25,350,screen)
lvl3block7 = Block(lightGray,winWidth - 100,400,25,100,screen)
lvl3block8 = Block(lightGray,winWidth - 300,300,25,100,screen)
lvl3block9 = Block(lightGray,375,275,175,20,screen)
lvl3spike1 = Spikes(black,200,winHeight - 100,225,winHeight-125,250,winHeight-100,screen)
lvl3spike2 = Spikes(black,600,winHeight-80,625,winHeight - 150,650,winHeight - 80,screen)
lvl3spike3 = Spikes(black,winWidth - 275,175,winWidth - 250,115,winWidth - 225,175,screen)
lvl3blocks.add(lvl3block1,lvl3block2,lvl3block3,lvl3block4,lvl3block5,lvl3block6,lvl3block7,lvl3block8,lvl3block9)
lvl3spikes.add(lvl3spike1,lvl3spike2,lvl3spike3)
lvl3 = Level(lvl3blocks,lvl3spikes,10,winHeight - 300)
levelList.append(lvl3)

#Level 4
lvl4blocks = pygame.sprite.Group()
lvl4spikes = pygame.sprite.Group()
lvl4block1 = Block(lightGray,winWidth - 100,winHeight - 25,25,100,screen)
lvl4block2 = Block(lightGray,winWidth - 425,winHeight - 25,25,200,screen)
lvl4block3 = Block(lightGray,winWidth - 800,winHeight - 75,75,190,screen)
lvl4block4 = Block(lightGray,0,100,winHeight-100,50,screen)
lvl4block5 = Block(lightGray,250,325,25,100,screen)
lvl4block6 = Block(lightGray,50,425,25,50,screen)
lvl4block7 = Block(lightGray,500,325,25,100,screen)
lvl4block8 = Block(lightGray,350,100,125,150,screen)
lvl4block9 = Block(lightGray,50,150,25,100,screen)
lvl4block10 = Block(lightGray,winWidth-200,250,25,100,screen)
lvl4block11 = Block(lightGray,500,175,25,50,screen)
lvl4block12 = Block(lightGray,winWidth-100,0,275,25,screen)
lvl4spike1 = Spikes(black,winWidth - 275,winHeight - 25,winWidth - 250,winHeight - 50,winWidth - 225,winHeight - 25,screen)
lvl4spike2 = Spikes(black,winWidth - 375,winHeight - 25,winWidth - 350,winHeight - 50,winWidth - 325,winHeight - 25,screen)
lvl4spike3 = Spikes(black, winWidth-610,winHeight-75,winWidth - 510,winHeight - 36,winWidth - 610, winHeight,screen)
lvl4spike4 = Spikes(black,400,225,425,275,450,225,screen)
lvl4spike5 = Spikes(black,winWidth-100,200,winWidth-150,225,winWidth-100,250,screen)
lvl4blocks.add(lvl4block1,lvl4block2,lvl4block3,lvl4block4,lvl4block5,lvl4block6,lvl4block7,lvl4block8,lvl4block9,
               lvl4block10,lvl4block11,lvl4block12)
lvl4spikes.add(lvl4spike1,lvl4spike2,lvl4spike3,lvl4spike4,lvl4spike5)
lvl4 = Level(lvl4blocks,lvl4spikes,winWidth - player.width - 10, winHeight - 200)
levelList.append(lvl4)

#Level 5
lvl5blocks = pygame.sprite.Group()
lvl5spikes = pygame.sprite.Group()
lvl5block1 = Block(black,325,10,75,15,screen)
lvl5block2 = Block(black,425,10,75,15,screen)
lvl5block3 = Block(black,325,150,20,115,screen)
lvl5block4 = Block(black,310,100,50,15,screen)
lvl5block5 = Block(black,440,100,50,15,screen)
lvl5block6 = Block(lightBlue,winWidth / 2 - player.width * 2, winHeight / 2 - player.height,player.height,player.width,screen)
lvl5block7 = Block(lightBlue,winWidth / 2 - player.width,winHeight / 2 - player.height - 25, 25,player.width,screen)
lvl5block8 = Block(lightBlue,winWidth / 2,winHeight / 2 - player.height, player.height,player.width,screen)
lvl5block9 = Block(lightBlue,winWidth / 2 - player.width,winHeight / 2, 25,player.width,screen)
lvl5blocks.add(lvl5block1,lvl5block2,lvl5block3,lvl5block4,lvl5block5,lvl5block6,lvl5block7,lvl5block8,lvl5block9)
lvl5spikes.add()
lvl5 = Level(lvl5blocks,lvl5spikes,winWidth / 2 - player.width, winHeight / 2 - player.height)
levelList.append(lvl5)

while inGame:
    player.curSpawnX = levelList[curLev].spawnX
    player.curSpawnY = levelList[curLev].spawnY
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