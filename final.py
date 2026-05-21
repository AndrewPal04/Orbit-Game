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
from classes import Player
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
        break
    if play2.draw():
        pass
    if play3.draw():
        pass

    pygame.display.update()
    clock.tick(60)

if level == 1:
    #moving backgrounds
    stars1 = Background(screen, starsIMG, 5, 500 ,300)
    stars2 = Background(screen, starsIMG, 5, 500, 300)
    stars2.rect.left = stars1.rect.right
    #Player
    shipIMG = pygame.image.load("WAVE.png")
    ship = Player(shipIMG, .04 , 500 , 300)

    sprite_group = pygame.sprite.Group()
    sprite_group.add(ship)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        stars1.rect.x -= 4
        stars2.rect.x -= 4
        
        if stars1.rect.right < 0:
            stars1.rect.left = stars2.rect.right
        if stars2.rect.right < 0:
            stars2.rect.left = stars1.rect.right
        stars1.draw()
        stars2.draw()
        sprite_group.draw(screen)
        sprite_group.update()

        top = pygame.draw.rect(screen,(165, 169, 180), (0,0,1000,100))
        bottom = pygame.draw.rect(screen, (165, 169, 180), (0,500,1000,100))
        
        #stop player from going too high or low
        if ship.rect.top <= 100:
            ship.rect.top = 100
        if ship.rect.bottom >= 500:
            ship.rect.bottom = 500

        pygame.display.update()
        clock.tick(60)
        
elif level == 2: #GRAVITY GUY GAME: goes from top to bottom, or bottom to top (gear player image)
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
For your homework, I want you to plan and design a couple
of obstacles that the user will have to dodge in every level.
You can make different obstacles for each level, or use the
same ones in all of them. Once you create the obstacle, try 
to put it on the screen, and make it move left so it flies
past the user dodging it.
Good Luck!
"""