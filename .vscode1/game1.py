from email import message
from itertools import count
from re import X
from tkinter import Y
import pygame
import random
import time
pygame.init()
clock=pygame.time.Clock()
#game_display surface
gd =pygame.display.set_mode((800,600))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
lightgreen=(0,155,0)
green=(0,255,0)
grey=(119,118,110)
car_image=pygame.image.load("car.jpg")
car_image=pygame.transform.scale(car_image,(100,100))
background=pygame.image.load("background1.jpg")
grass=pygame.image.load("download12.jpg")

def Message(size,mess,x_pos,y_pos):
    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,white)
    gd.blit(render , (x_pos, y_pos))
    

Message(100,"START",150,100)
clock.tick(1)

def car(X,Y):
    gd.blit(car_image,(X,Y))
    gd.blit(grass,(0,0))
    gd.blit(grass,(700,0))
    if 0<X<90 or 700<X+90:
        Message(100, "GAME-OVER" , 200,200)
        pygame.display.update()
        clock.tick(0.35)
        Game_intro()

def enemycar(X_r,Y_r):
    gd.blit(car_image,(X_r,Y_r))
   

def button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,green,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
         pygame.draw.rect(gd,lightgreen,[x_button,y_button,100,30])
         Message(50,mess_b,x_button,y_button)
         if click==(1,0,0) and mess_b=="PLAY":
            Game_loop()
         elif click==(0,0,1) and mess_b=="QUIT":
            pygame.quit()
            quit()
            
def  car_crash(X,X_r,Y,Y_r):
    if X_r<X<X_r+90 and Y_r<Y<Y_r+90 or X_r<X+100<X_r+90 and Y_r<Y<Y_r+90 :
        Message(100,"CRASHED!",200,200)
        pygame.display.update()
        time.sleep(1)
        Game_intro()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   

def score(count):
    font= pygame.font.SysFont(None,30)
    screen_text= font.render('Score:' + str(count), True,white)
    gd.blit(screen_text,(0,0))
   


def Game_intro():
    
    intro=False
    while intro==False:
        gd.blit(background,(0,0))
        button(100,300,"PLAY")
        button(600,300,"QUIT")
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        
        pygame.display.update()

def Game_loop():
   X=300
   Y=490
   count=0
   X_change=0
   Y_change=0
   X_r=random.randrange(100,600)
   Y_r=0



   game_over=False
   while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                X_change=+5
            elif event.key==pygame.K_RIGHT:

                X_change=-5

            elif event.key==pygame.K_UP:
                Y_change=+5
            elif event.key==pygame.K_DOWN:
                Y_change=-5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN :
                X_change=0
                Y_change=0

    gd.fill(grey)
    car(X,Y)
    score(count)
    enemycar(X_r,Y_r)
    Y_r+=10
    if Y_r==600:
        Y_r=0
        X_r=random.randrange(100,600)
        count+=1

    car_crash(X,X_r,Y,Y_r)    
    X=X-X_change
    Y=Y-Y_change
    clock.tick(50)
    pygame.display.update()



Game_intro( )
pygame.display.update()
pygame.quit()
quit()