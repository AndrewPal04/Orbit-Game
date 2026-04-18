"""
space waves
-a spike dodging game where you have to dodge spikes coming at you in space, the longer you survive the higher your score
"""
import pygame
import random
from classes import Background
from classes import Button
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))

#Create objects
starsIMG = pygame.image.load("stars.png")
stars = Background(screen, starsIMG, 5, 500, 300)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace
    stars.draw()




    pygame.display.update()
    clock.tick(60)

