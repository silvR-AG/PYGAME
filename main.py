from pickle import FALSE, TRUE
from turtle import distance
import pygame
import random
import math


#pygame initialization
pygame.init()


#pygame screen creation
screen= pygame.display.set_mode((1280,720))


#Background
background = pygame.image.load('background.jpg')


#Title and icon
pygame.display.set_caption(('THE CAT&RAT'))
icon=pygame.image.load('games-icon-png-4.png')
pygame.display.set_icon((icon))



#Player
playerImg = pygame.image.load('icons8-year-of-tiger-100.png')
playerX = 600
playerY = 600
playerX_change = 0
playerY_change = 0

#Player2
player2Img = pygame.image.load('icons8-rat-100.png')
player2X = random.randint(111,1111)
player2Y = random.randint(99,599)
player2X_change = 0
player2Y_change = 0

#Bullet
# BulletImg = pygame.image.load('settings.png')
# BulletX = 600
# BulletY = 600
# BulletX_change = 0
# BulletY_change = 0
# Bullet_state = "ready"



#Players functions
def player(X,Y):
    screen.blit(playerImg, (X,Y))
def player2(X,Y):
    screen.blit(player2Img, (X,Y))



#Text Display
font=pygame.font.Font('freesansbold.ttf',100)
font1=pygame.font.Font('freesansbold.ttf',32)
font2=pygame.font.Font('freesansbold.ttf',20)
textX = 300
textY = 300
def showText(X,Y):
    win = font.render('Player 1 Wins',True,(200,255,180))
    screen.blit(win, (X,Y))
score_value = 0
def showScore():
    score = font1 .render("Score:" +str(score_value), True, (255,255,255))
    screen.blit(score, (100,0))
    exittext = font2.render("Close window to end the Game", True, (255,255,255))
    screen.blit(exittext, (900,10))


#Bullet fire function



#Collide function
def isCol(playerX,playerY,player2X,player2Y):
    distance=math.sqrt((math.pow(player2X-playerX,2))+(math.pow(player2Y-playerY,2)))
    if distance<20:
        return True
    else:
        return False



#Game Loop
running=True
while running:
    screen.fill((255, 255, 255)) #RGB Color Codes
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

#Game movement for players
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change = -0.35
            if event.key==pygame.K_RIGHT:
                playerX_change = 0.35
            if event.key==pygame.K_UP:
                playerY_change = -0.35
            if event.key==pygame.K_DOWN:
                playerY_change = 0.35
            if event.key==pygame.K_a:
                player2X_change = -0.6
            if event.key==pygame.K_d:
                player2X_change = 0.6
            if event.key==pygame.K_w:
                player2Y_change = -0.6
            if event.key==pygame.K_s:
                player2Y_change = 0.6
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                playerY_change = 0
            if event.key==pygame.K_a or event.key==pygame.K_d:
                player2X_change = 0
            if event.key==pygame.K_w or event.key==pygame.K_s:
                player2Y_change = 0
    playerX += playerX_change
    playerY += playerY_change
    player2X += player2X_change
    player2Y += player2Y_change

#Creating boundary for players 
    if playerX<50:
        playerX=50
    elif playerX>1230:
        playerX=1230
    if playerY<0:
        playerY=0
    elif playerY>620:
        playerY=620
    if player2X<50:
        player2X=50
    elif player2X>1230:
        player2X=1230
    if player2Y<0:
        player2Y=0
    elif player2Y>620:
        player2Y=620  

#Calling player functions
    player(playerX,playerY)
    player2(player2X,player2Y)

#Checking Collision
    collision = isCol(playerX,playerY,player2X,player2Y)
    if collision:
        #print("Player 1 wins")
        showText(textX,textY)
        score_value =+ 1
        # playerX = random.randint(111-1111)
        # playerY = random.randint(99,699)
        # player2X = random.randint(111,1111)
        # player2Y = random.randint(99,699)
    showScore()
    pygame.display.update() #Update Screen each time window reopens



