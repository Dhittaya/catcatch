import pygame
from pygame import *
import time
import random

pygame.init()

white = (255,255,255)
blue = (41, 103, 203)

catl_x = 45
catr_x = 305
cat_y = 517

screen = pygame.display.set_mode([500,800])

# This sets the name of window
pygame.display.set_caption('Cat Catch')

# Play background music
pygame.mixer.music.load('fatcat.mp3')
pygame.mixer.music.set_volume(0.3)


clock = pygame.time.Clock()

# Set position
background_position = [0,0]

# Load and set up graphics
background_image = pygame.image.load('bg.png').convert()
cat1_eat_image = pygame.image.load('eat.png')
catl_miss_image = pygame.image.load('miss.png')
fish_image = pygame.image.load('fish.png')

font = pygame.font.SysFont('comicsansms', 25)

def load_image(name):
    image = pygame.image.load(name)
    return image

def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0):
    textSurf, textRect = text_objects(msg,color)
    #screen_text = font.render(msg, True, color)
    #screen.blit(screen_text, (105,250))
    textRect.center = 500/2, (800/2 + y_displace)
    screen.blit(textSurf, textRect)

def guide():
    status = 1
    guide = False
    guide1 = load_image('guide1.png')
    guide2 = load_image('guide2.png')
    guide3 = load_image('guide3.png')
    screen.blit(background_image, background_position)
    screen.blit(guide1, background_position)
    while not guide:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n and status == 2:
                screen.blit(guide3, background_position)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n and status == 1:
                status = 2
                screen.blit(guide2, background_position)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                intro()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                quit()
                guide = True        
        pygame.display.update()
        clock.tick(15)
    
def intro():
    intro = True
    catl = load_image('cat.png')
    catr = load_image('cat.png')
    catcatch = load_image('catcatch.png')

    while intro:
        screen.blit(background_image, background_position)
        screen.blit(catcatch, (93,100))
        message_to_screen('Press F to start! or Press G to guide',
                          blue,
                          y_displace=30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                   guide()
                    
                if event.key == pygame.K_f:
                    intro = False
                    gameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
        screen.blit(catl, (catl_x,cat_y))
        screen.blit(catr, (catr_x,cat_y))
        pygame.display.update()
        clock.tick(15)

def gameLoop():
    pygame.mixer.music.play(-1)
    
    fish_image = pygame.image.load('fish.png')
    statusfish = "normal"
    gameExit = False
    gameOver = False
    catl = load_image('cat.png')
    catr = load_image('cat.png')
    gameover = load_image('gameover.png')

    # Fish
    status_eatl = ""
    fish_startx = -100
    fish_starty = random.randrange(100, 200)
    fish_speed = 8.5
    gravity = 0.285
    speed = 0
    time = 0
    red = (255,0,0)
    black = (0,0,0)
    # Fish Right
    status_eat = ""
    fish_imager = pygame.image.load('fishr.png')
    statusfishr = "normal"
    fish_startxr = 500
    fish_startyr = random.randrange(100, 200)
    fish_speedr = 8.3
    gravityr = 0.33
    speedr = 0

    score = 0
    
    while not gameExit:
        while gameOver == True:
            
            screen.blit(background_image, background_position)
            screen.blit(gameover, (120,220))
            font = pygame.font.SysFont("comicsansms", 40)
            text = font.render("Your Score is: "+str(score), True, white)
            screen.blit(text,(100,100))
            message_to_screen("Press F to play again or Q to quit",
                              red,
                              y_displace=80)
            screen.blit(catl, (catl_x,cat_y))
            screen.blit(catr, (catr_x,cat_y))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_f:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                keystate = pygame.key.get_pressed()
                if event.key == pygame.K_LEFT:
                    catl = pygame.image.load('eat.png')
                    status_eat = "eat"
                elif event.key == pygame.K_RIGHT:
                    status_eatl = "eat"
                    catr = pygame.image.load('eat.png')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    catl = pygame.image.load('cat.png')
                    status_eat = ""
                elif event.key == pygame.K_RIGHT:
                    status_eatl = ""
                    catr = pygame.image.load('cat.png')
        class Sprite:
 
            def __init__(self,x,y,width,height):
 
                self.x=x
 
                self.y=y
 
                self.width=width
 
                self.height=height
 

        def detectCollisions(x1,y1,w1,h1,x2,y2,w2,h2):
 
            if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
 
                return True
 
            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
 
                return True
 
            elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
 
                return True
 
            elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
 
                 True
 
            else:
 
                return False
        def things_score(count):
            font = pygame.font.SysFont('comicsansms', 50)
            text = font.render("score "+str(count), True, white)
            screen.blit(text,(0,0))

        Sprite1=Sprite(90,570,50,50) #box mouth left
        Sprite2=Sprite(350,570,50,50) #box mouth right
        
        # Copy image to screen
        
        screen.blit(background_image, background_position)
        screen.blit(catl, (catl_x,cat_y))
        screen.blit(catr, (catr_x,cat_y))
        # Fish
        
        screen.blit(fish_image, (fish_startx, fish_starty))
        speed += gravity
        fish_startx += fish_speed
        fish_starty += speed
        
        #Fish right
        screen.blit(fish_imager, (fish_startxr, fish_startyr))
        speedr += gravityr
        fish_startxr -= fish_speedr
        fish_startyr += speedr
        
        if fish_startx > 500:
            fish_startx = -100
            speed = 0
            fish_starty = random.randrange(100, 200)
            if (statusfish == "normal") and (random.randrange(0, 20) > 15):
                fish_image = pygame.image.load('gfish.png')
                statusfish = "gold"
            
            elif statusfish == "normal" and (random.randrange(0, 20) < 10):
                fish_image = pygame.image.load('bomb.png')
                statusfish = "bomb"
            elif (statusfish == "gold") or (statusfish == "bomb"):
                fish_image = pygame.image.load('fish.png')
                statusfish = "normal"
        if fish_startxr < 0:
            fish_startxr = 500
            speedr = 0
            fish_startyr = random.randrange(100, 200)
            if (statusfishr == "normal") and (random.randrange(0, 20) > 15):
                fish_imager = pygame.image.load('gfishr.png')
                statusfishr = "gold"
            
            elif statusfishr == "normal" and (random.randrange(0, 20) < 10):
                fish_imager = pygame.image.load('bomb.png')
                statusfishr = "bomb"
            elif (statusfishr == "gold") or (statusfishr == "bomb"):
                fish_imager = pygame.image.load('fishr.png')
                statusfishr = "normal"

        if detectCollisions(Sprite1.x,Sprite1.y,Sprite1.width,Sprite1.height-30,fish_startxr,fish_startyr,50,30): #eat left
            if status_eat == "eat":
                speedr+=50
                fish_startxr = 600
                if statusfishr == "normal":
                    score += 1
                if statusfishr == "gold":
                    score += 2
                if statusfishr == "bomb":
                    catl = pygame.image.load('burn.png')
                    pygame.time.delay(500)
                    gameOver = True
            elif statusfishr == "normal":
                catl = pygame.image.load('miss.png')
                catr = pygame.image.load('miss.png')
                gameOver = True
            else:
                speedr -= 10
            
            
        if detectCollisions(Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height-30,fish_startx,fish_starty,50,30) :#eat right
            if status_eatl == "eat":
                speed += 100
                fish_startx = -200
                if statusfish == "normal":
                    score += 1
                if statusfish == "gold":
                    score += 2
                if statusfish == "bomb":
                    catr = pygame.image.load('burn.png')
                    pygame.time.delay(500)
                    gameOver = True
            elif statusfish == "normal":
                catl = pygame.image.load('miss.png')
                catr = pygame.image.load('miss.png')
                gameOver = True
            else:
                speed -= 10
               
        things_score(score)
        
        pygame.display.update()
        
        if score <= 25:
            clock.tick(60)
        elif score <= 50:
            clock.tick(70)
        elif score <= 75:
            clock.tick(75)
        elif score >= 100 :
            clock.tick(80)
        elif score >= 150 :
            clock.tick(83)
        elif score >= 175 :
            clock.tick(85)
        elif score >= 200 :
            clock.tick(90)
            
    pygame.quit()
    quit()
intro()
guide()
gameLoop()
