"""
space waves
-a spike dodging game where you have to dodge spikes coming at you in space, the longer you survive the higher your score

Github: https://github.com/AndrewPal04/Orbit-Game
"""
import pygame
import time
import random
from classes import Background
from classes import Button
from classes import Text
from classes import Player
from classes import Obstacle
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
    ship = Player(shipIMG, .03 , 500 , 300)

    #Obstacles
    spikeIMG = pygame.image.load("spikeTop.png")
    spikeBIMG = pygame.image.load("spikeBottom.png")
    mineIMG = pygame.image.load("mine.png")
    spike1 = Obstacle(spikeIMG, .1, 800, 140)
    spike2 = Obstacle(spikeBIMG, .1, 1000, 460)
    spike3 = Obstacle(spikeBIMG, .1, 200, 460)
    spike4 = Obstacle(spikeIMG, .1, 300, 140)
    mine1 = Obstacle(mineIMG, .03, 2000, 300)

    sprite_group = pygame.sprite.Group()
    sprite_group.add(ship)
    sprite_group.add(spike1)
    sprite_group.add(spike2)
    sprite_group.add(spike3)
    sprite_group.add(spike4)
    sprite_group.add(mine1)
    start = time.time()
    win = False
    while True:
        end = time.time()
        timePassed = end-start
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        if timePassed > 50:
            win = True
            break
        stars1.rect.x -= 4
        stars2.rect.x -= 4
        spike1.rect.x -= 4
        spike2.rect.x -= 4
        spike3.rect.x -= 4
        spike4.rect.x -= 4
        mine1.rect.x -= 4
        
        if stars1.rect.right < 0:
            stars1.rect.left = stars2.rect.right
        if stars2.rect.right < 0:
            stars2.rect.left = stars1.rect.right

        if spike1.rect.right <0:
            spike1.rect.left = random.randint(1000,1400)
        if spike2.rect.right <0:
            spike2.rect.left = random.randint(1000,1400)
        if spike3.rect.right <0:
            spike3.rect.left = random.randint(1000,1400)
        if spike4.rect.right <0:
            spike4.rect.left = random.randint(1000,1400)
        if mine1.rect.right <0:
            mine1.rect.left = random.randint(1500,2000)
            mine1.rect.y = random.randint(200,400)

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

        if pygame.sprite.collide_rect(ship, spike1):
            print("Collided with Spike!")
            break
        if pygame.sprite.collide_rect(ship, spike2):
            print("Collided with Spike!")
            break
        if pygame.sprite.collide_rect(ship, spike3):
            print("Collided with Spike!")
            break
        if pygame.sprite.collide_rect(ship, spike4):
            print("Collided with Spike!")
            break
        if pygame.sprite.collide_rect(ship, mine1):
            print("Collided with Mine!")
            break

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


if win:
    winText = Text(screen, "YOU WIN!", (247, 194, 2), 500, 300, 100)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Draw win text
        stars.draw()
        winText.draw()

        pygame.display.update()
        clock.tick(60)

"""
Homework
For homework I want you to use the following link
to begin making your final presentation for your project!
https://docs.google.com/presentation/d/1SvjGVSDHrpJ3E__emNbEpPLVFicQvc0u9rTCRFXXVmg/edit?usp=sharing
Create a copy of the slides, and fill in as much as you can
so far for your project! Try to add in pictures that you use in your project
to make it look as cool as possible, and fill out at least
4 of the slides for homework.
Good Luck!
"""