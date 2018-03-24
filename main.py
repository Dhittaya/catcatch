import pygame
from pygame import *

pygame.init()

screen = pygame.display.set_mode([500,800])

# This sets the name of window
pygame.display.set_caption('Cat Catch')

clock = pygame.time.Clock()

# Set position
background_position = [0,0]

# Lodev and set up graphics
background_image = pygame.image.load('bg.png').convert()
cat1_image = pygame.image.load('cat.png')
catr_image = pygame.image.load('cat.png')


def catl(catl_x, cat_y):
    screen.blit(cat1_image, (catl_x, cat_y))
def catr(catr_x, cat_y):
    screen.blit(catr_image, (catr_x, cat_y))

def gameLoop():
    catl_x = 45
    catr_x = 305
    cat_y = 517
    done = False
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Copy image to screen
        screen.blit(background_image, background_position)
        catl(catl_x,cat_y)
        catr(catr_x,cat_y)
        
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()
gameLoop()
