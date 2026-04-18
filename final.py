"""
space waves
-a spike dodging game where you have to dodge spikes coming at you in space, the longer you survive the higher your score

Github: https://github.com/AndrewPal04/Orbit-Game
"""
import pygame
import random
from classes import Background
from classes import Button
from classes import Text
pygame.init()

# print(pygame.font.get_fonts())

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))

#Create objects
starsIMG = pygame.image.load("stars.png")
stars = Background(screen, starsIMG, 5, 500 ,300)

playimg = pygame.image.load("play.png")
play = Button(screen, playimg, 1,500, 400)

t = Text(screen, "Orbit", (247,194,2), 500, 100, 200)


#Start Screen
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace
    stars.draw()
    if play.draw():
        break 
    t.draw()


    pygame.display.update()
    clock.tick(60)

#Level select screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace
    screen.fill((0,0,0))



    pygame.display.update()
    clock.tick(60)


"""
Homework
Now that we've set up our play button screen, I want you
try to and create the level selection screen. You will need
to get a background, as well as 3 different level buttons.
You might also want to name them using a text class.
Good Luck!
"""