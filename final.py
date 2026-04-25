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

#objects
lvl1IMG = pygame.image.load("lvl1.png")
lvl1 = Background(screen, lvl1IMG, 0.439,175,200)
lvl2imh = pygame.image.load('lvl2.png')
lvl2 = Background(screen, lvl2imh,0.90,500,200.2335876478574385479)
lvl3qqq = pygame.image.load('lvl3.png')
lvl3 = Background(screen, lvl3qqq, 0.305,820,200)

play1 = Button(screen, playimg, 0.68,175, 400)
play2 = Button(screen, playimg, 0.68,500, 400)
play3 = Button(screen, playimg, 0.68,820, 400)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    #workspace
    stars.draw()
    rect1 = pygame.draw.rect(screen, (222, 255, 184),(50, 70,250,500))
    rect2 = pygame.draw.rect(screen, (222, 255, 184),(375, 70,250,500))
    rect3 = pygame.draw.rect(screen, (222, 255, 184),(700, 70,250,500))
    lvl1.draw()
    lvl2.draw()
    lvl3.draw()

    if play1.draw():
        level = 1
    if play2.draw():
        pass
    if play3.draw():
        pass

    pygame.display.update()
    clock.tick(60)

if level == 1:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)
elif level == 2:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)
else:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(60)

"""
Homework
Since we will be starting on the levels in our next class, I want you
to design our main character that will be navigating through the maps.
You can create multiple designs, so users can select their favorite,
and use it in the program. Make sure to save it as a .png, and put the
image in the replit so we can use it next week.
Good Luck!
"""