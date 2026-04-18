# python 3
# email: codingminds8@gmail.com
# pass:  Codingminds29

# Creating a class with attributes

# class Dog:
#     def __init__(self, name, age, color, type):
#         self.name = name
#         self.age = age
#         self.color = color
#         self.type = type
#     #Creating methods
#     def bark(self):
#         print(self.name,"barked!")
#     #Creating a method with a parameter
#     def fetch(self, item):
#         print(self.name,"brought you a", item)

# #Creating an object
# dog1 = Dog("Luna",2,"brown","pitbull")

# dog2 = Dog("q",-100000000000000000000,"www","qwerty")

# print("My dog is named", dog1.name)

# #Say my dog's name is ___ and he is ___ years old

# print("my dog's name is", dog2.name,"and he's", dog2.age,  "years old" )

# #Changing attributes
# print(dog1.name,"had her birthday!")
# dog1.age += 1
# print(dog1.name,"is now",dog1.age, "years old")

# #Change the name of your dog, and say "i renamed my dog to ___"
# dog2.name = "qq"
# print("i renamed my dog to",dog2.name)

# #Using methods
# dog1.bark()
# dog2.bark()

# #using methods with parameters
# dog1.fetch("stick")
# dog2.fetch("ejinknefuiveeonvbhr")

# dog3=Dog("Clifford",4,"red","big")
# dog3.bark()

# Create a new class for a Vehicle
# The class should have attributes for color, and year. You can add more if you want

# Make a method for Drive, where it says "Your ____ drove forward"


# class Vehicle:

#     def __init__(self, color, type, year):
#         self.year = year
#         self.color = color
#         self.type = type

#     def drive(self):
#         print("Your", self.type, 'drove backwards')

#     def honk(self):
#         print(self.type, "honked!")


# # #Create a vehicle with real attributes

# Vhicle = Vehicle("white", "Tesla", 2026)
# car = Vehicle("silver", "Corvette", 2020)

# Vhicle.drive()
# car.drive()


# #Inheriting from Vehicle class
# class Truck(Vehicle):

#     def __init__(self, color, type, year):
#         Vehicle.__init__(self, color, type, year)
#         self.stuff = []

#     def putStuff(self, item):
#         self.stuff.append(item)
#         print("You put a", item, "in your truck!")


# truck1 = Truck("blue", "honda", 2011)

# truck1.drive()
# truck1.putStuff("json file")
# truck1.putStuff("txt file")
# print(truck1.stuff)


# LEMONADE STAND

# Make a method that makes a cup of lemonade
# the lemonade stand needs to have lemon, ice, and sugar to make it

# class Lemonade:
#     def __init__(self, name, cash, cups, lemon, ice, sugar, price):
#         self.name=name
#         self.cash=cash
#         self.cups=cups
#         self.lemon=lemon
#         self.sugar=sugar
#         self.price=price
#         self.ice=ice

#     def sell(self):
#         if self.cups>0:
#             self.cups -= 1
#             self.cash += self.price
#             print(self.name,"sold a cup of lemonade for $"+str(self.price)+"!")
#         else:
#             print(self.name,"ran out of lemonade... make some more!")

#     def make(self):
#         if self.ice>0 and self.lemon>0 and self.sugar>0:
#             self.ice -= 1
#             self.lemon -= 1
#             self.sugar-=1
#             self.cups += 1
#             print("You made a cup of lemonade!")
#         else:
#             if self.ice <= 0:
#                 print("You need to restock on ice")
#             if self.lemon <= 0:
#                 print("You need to restock on lemon")
#             if self.sugar <= 0:
#                 print("You need to restock on sugar")

#     def buy(self):
#         if self.cash >=2:
#             self.cash -=2
#             self.ice += 1
#             self.lemon += 1
#             self.sugar+=1
#             print("you spent $2 to get one of every ingredient!")
#         else:
#             print("not enough money to restock")

#     def s(self):
#         print("Cups: {}".format(self.cups))
#         print('Money: ${}'.format(self.cash))


# stand = Lemonade("The Lemonade", 10, 10, 10, 10, 10, 2.5)

# # """
# # Classwork/Homework

# # Right now in the game, when you run out of ice, lemon, and sugar
# # you can't get more. Make a method called restock, that costs $2
# # and gives you 1 ice, lemon, and sugar.
# # ALSO, make a method called stats, that prints out
# # Name: ___
# # Cash: ___
# # Price: ___
# # Cups: ___
# # ice: ___
# # etc.
# # After you make the methods, make it so there are options to
# # restock, and see stats in the while loop
# # Good Luck!

# # """
# import time, os

# while True:
#     time.sleep(0.2)
#     os.system("clear")
#     print("1. Sell lemonade\n2. Make lemonade\n3. Restock ingredients\n4. Stats\n5. Quit")
#     choice = str(input("> "))

#     if choice == "1":
#         stand.sell()
#     elif choice =="2":
#         stand.make()
#     elif choice =="3":
#         stand.buy()
#     elif choice=="4":
#         stand.s()
#         time.sleep(1)
#     elif choice =="5":
#         break

#     else:
#         print("Invalid option...")


# PYGAME

# in terminal: pip install pygame

# import pygame

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000, 600))# width, height

# # #Game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((50,50,50))
#     #rectangles/squares
#     #var = pygame.draw.rect(surface, (R,G,B), (X,Y, width, height))
#     redRectangle = pygame.draw.rect(screen, (200,13,43),(10, 20, 100, 50))

#     rectangle2 = pygame.draw.rect(screen, (22,255,254),(200, 200, 200, 100))
#     #circles
#     #var = pygame.draw.circle(surface, (R,G,B), (X,Y), radius)
#     ssksskksksks = pygame.draw.circle(screen, (0,255,0), (500,300), 50)

#     #lines
#     #var = pygame.draw.line(surface, (R,G,B), (startX, startY), (endX, endY), thickness)
#     line1 = pygame.draw.line(screen, (10,10,200), (0,0), (500, 300), 5)

#     pygame.display.update()
#     clock.tick(60)


# Create a brand new pygame loop
# In the loop, draw a blue sky with white clouds


# BASIC LOOP
# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     pygame.display.update()
#     clock.tick(60)


# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((135,200,250))
#     var1 = pygame.draw.circle(screen, (255,255,255), (200,100), 50)
#     var2 = pygame.draw.circle(screen, (255,255,255), (250,150),50)
#     var3 = pygame.draw.circle(screen, ()55,255,25)


#     pygame.display.update()
#     clock.tick(60)


"""
To use vs code you need to:
download vs code
https://www.youtube.com/watch?v=zK1rKC7QVwk
download python (Make sure to select ADD TO PATH)
https://www.youtube.com/watch?v=8mO6QXOcpqU
pip install pygame (in terminal)
make fun projects
"""

# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((135,200,250))
#     #cloud
#     var1 = pygame.draw.circle(screen, (255,255,255), (200,100), 50)
#     var2 = pygame.draw.circle(screen, (255,255,255), (250,150),50)
#     var3 = pygame.draw.circle(screen, (255,255,255), (300,200),50)

#     grass = pygame.draw.rect(screen, (0,255,0), (0,500,1000,100))

#     yellow_triangle = pygame.draw.polygon(screen, (248, 252, 3), [(10, 300), (40, 200), (70, 300) ]) # surface, color, list of points
#     blue_triangle = pygame.draw.polygon(screen, (0,0,100), [(200, 600), (300,400), (400, 80)])
#     pygame.display.update()
#     clock.tick(60)


# KEYSTATE

# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     screen.fill((100,100,200))

#     #THIS TRACKS YOUR KEYS
#     #lINK FOR CODES: https://www.pygame.org/docs/ref/key.html
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_a]:
#         var1 = pygame.draw.circle(screen, (255,255,255), (200,100), 50)
#         var3 = pygame.draw.circle(screen, (200,200,200), (200, 100), 40)
#     if keystate[pygame.K_b]:
#         var2 = pygame.draw.rect(screen, (255, 0 ,0), (300,300,200,200))


#     pygame.display.update()
#     clock.tick(61)

# up and down arrows do stuff example:
# hint: Up arrow code is pygame.K_UP, down arrow is pygame.K_DOWN


#     screen.fill((100,100,200))
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_UP]:
#         var1 = pygame.draw.rect(screen, (255, 0 , 0), (300,300,200,200))

#     if keystate[pygame.K_DOWN]:
#         var2 = pygame.draw.circle(screen, (0,255,0), (500,300), 50)
#     pygame.display.update()
#     clock.tick(61)


# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #Workspace
#     screen.fill((100,100,200))
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_w]:
#         var1 = pygame.draw.circle(screen, (255,0,0) , (500,100),50)
#     if keystate[pygame.K_a]:
#         var2 = pygame.draw.rect(screen, (66,135,245),(50,300,100,50))
#     if keystate[pygame.K_s]:
#         var3 = pygame.draw.polygon(screen, (0, 255, 0), [(200,150), (300,100), (400,150), (350,300), (250,300)], 0)
#     if keystate[pygame.K_d]:
#         var4 = pygame.draw.line(screen, (255,255,255), (123,123), (500,300), 5)


#     pygame.display.update()
#     clock.tick(60)

# Class: Text
import pygame


class Text:
    def __init__(self, surface, text, color, x, y, size):
        font_name = pygame.font.match_font("gillsansultracondensed")
        self.surface = surface
        self.text = text
        self.size = size
        self.font = pygame.font.Font(font_name, self.size)
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surface.blit(text_surface, text_rect)


# using the text class:

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# #To see options:
# # print(pygame.font.get_fonts())

# #Create our object
# text1 = Text(screen, "Hello", (100,123,43),440, 100, 50)
# text2 = Text(screen, "world", (222,111,133), 560, 100, 50)
# text3 = Text(screen, "My name is Trevor", (0,0,0), 500, 300, 25)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((255,255,255))
#     #Using draw method
#     text1.draw()
#     text2.draw()
#     text3.draw()


#     pygame.display.update()
#     clock.tick(60)

"""
To use vs code you need to:
download vs code
https://www.youtube.com/watch?v=zK1rKC7QVwk
download python (Make sure to select ADD TO PATH)
https://www.youtube.com/watch?v=8mO6QXOcpqU
# screen = pygame.display.set_mode((1000,600))pip install pygame (in terminal)
make fun projects!
"""


"""
Make a new pygame loop where you use the text class
to draw something that says "press 'x' to draw a square".
Then use keystate to make it work
"""

# import pygame
# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# #create our objects
# text1 = Text(screen, "press x to draw a square", (0,0,0), 500, 300, 50)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     screen.fill((255,255,255))
#     text1.draw()
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_x]:
#         var1 = pygame.draw.rect(screen, (255,0,0), (450,350,100,100))


#     pygame.display.update()
#     clock.tick(60)

"""
Homework
I want you to copy over last week's homework below this comment, 
but now change the program so there are 4 different texts on the 
screen that tell you what to click so that you can draw a certain shape.
Make sure to tell the user the correct information so they know
what shape and what color they will make.
Good Luck!

#Extra:
Try to see if you can add a new shape, and a text to your game
Make a shape that has a color using random.randint(0,255)

"""


# import pygame
# from classes import Text

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# text1 = Text(screen,"press W to make a circle", (0,1,3), 500,200, 50)
# text2 = Text(screen,"press A to make a rect", (0,1,3), 500,300, 50)
# text3 = Text(screen,"press S to make a a polygon", (0,1,3), 500,400, 50)
# text4 = Text(screen,"press D to make a line", (0,1,3), 500,500, 50)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     #Workspace
#     screen.fill((100,100,200))
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_w]:
#         var1 = pygame.draw.circle(screen, (255,0,0) , (500,100),50)
#     if keystate[pygame.K_a]:
#         var2 = pygame.draw.rect(screen, (66,135,245),(50,300,100,50))
#     if keystate[pygame.K_s]:
#         var3 = pygame.draw.polygon(screen, (0, 255, 0), [(200,150), (300,100), (400,150), (350,300), (250,300)], 0)
#     if keystate[pygame.K_d]:
#         var4 = pygame.draw.line(screen, (255,255,255), (123,123), (500,300), 5)

#     text1.draw()
#     text2.draw()
#     text3.draw()
#     text4.draw()

#     pygame.display.update()
#     clock.tick(60)


# Playing Audio

# import pygame

# pygame.init()

# pygame.mixer.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))

# pygame.mixer.music.load("sound.mp3")
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     keystate = pygame.key.get_pressed()
#     if keystate[pygame.K_d]:
#         pygame.mixer.music.play()

#     pygame.display.update()
#     clock.tick(60)

# Class: Player (Sprite)
# import pygame, time


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        image,
        scale,
        x,
        y,
    ):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


#     def update(self, target):
#         if target.rect.x < self.rect.x:
#             self.rect.x -= 6
#         if target.rect.x > self.rect.x:
#             self.rect.x += 6
#         if target.rect.y < self.rect.y:
#             self.rect.y -= 6
#         if target.rect.y > self.rect.y:
#             self.rect.y += 6

#     def update2(self):
#         keystate = pygame.key.get_pressed()
#         if keystate[pygame.K_UP]:
#             self.rect.y -= 5
#         if keystate[pygame.K_DOWN]:
#             self.rect.y += 5
#         if keystate[pygame.K_RIGHT]:
#             self.rect.x += 5
#         if keystate[pygame.K_LEFT]:
#             self.rect.x -= 5
#         if self.rect.top > 600:
#             self.rect.bottom = 0
#         if self.rect.bottom < 0:
#             self.rect.top = 600
#         if self.rect.right < 0:
#             self.rect.left = 1000
#         if self.rect.left > 1000:
#             self.rect.right = 0


# pygame.init()

# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000,600))


# #Load in images
# monkeyIMG = pygame.image.load("monkey.png")
# monkeyzIMG = pygame.image.load("laMonkey.png")
# #Creating objects
# playeree = Player(monkeyIMG, 0.3, 100, 100)
# player2 = Player(monkeyzIMG, 0.1, 500, 300)


# sprite_group = pygame.sprite.Group()
# sprite_group.add(playeree)
# sprite_group.add(player2)


# tagText = Text(screen, "TAG", (22,22,21), 500,300, 100)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     screen.fill((200,100,100))
#     sprite_group.draw(screen)
#     playeree.update()
#     player2.update2()

#     if pygame.sprite.collide_rect(playeree, player2):
#         tagText.draw()
#         pygame.display.update()
#         time.sleep(2)

#         playeree.rect.x = 100
#         playeree.rect.y = 100
#         player2.rect.x = 900
#         player2.rect.y = 500

#     pygame.display.update()
#     clock.tick(60)

# Homework
# Make a brand new pygame loop where the user is steve
# from minecraft, and there's another sprite that is a
# a skeleton. Put them both on the screen, and when
# the skeleton catches steve, write "You Died!" on the
# screen, and end the pygame loop with pygame.quit and quit.
# Good Luck!

# pygame.init()
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode((1000, 600))
# # load in images
# laSketetonIMG = pygame.image.load("laSkeleton.png")
# steveIMG = pygame.image.load("steve.png")
# # create players
# w = Player(laSketetonIMG, 0.1, 100, 100)
# a = Player(steveIMG, 0.1, 500, 300)

# sprite_group = pygame.sprite.Group()
# sprite_group.add(w)
# sprite_group.add(a)
# hitText = Text(screen, "****got shot by an arrow", (22, 22, 21), 500, 300, 50)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     # workspace
#     screen.fill((200, 100, 100))
#     sprite_group.draw(screen)
#     w.update(a)
#     a.update2()
#     if pygame.sprite.collide_rect(w, a):
#         hitText.draw()
#         pygame.display.update()
#         time.sleep(2)
#         pygame.quit()
#         quit()

#     pygame.display.update()
#     clock.tick(60)


# Class: Button
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, surface, image, scale, x, y):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.surface = surface
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self):
        self.surface.blit(self.image, (self.rect.x, self.rect.y))
        pressed = False 
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                pressed = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False 
        return pressed

#Testing the button
pygame.init()
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

# #Making the button
# cookieIMG = pygame.image.load("cookie.png")
# cookie = Button(screen, cookieIMG, 0.25, 500, 100)

# #make a button that makes the background red if you press it
# lm = pygame.image.load("laMonkey.png")
# m = Button(screen, lm, 0.5, 500 ,400)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     #workspace
#     if cookie.draw():
#         screen.fill((0,50,250))
#     if m.draw():
#         screen.fill((255, 0 ,0))

#     pygame.display.update()
#     clock.tick(60)

#New Game using Buttons:
# import random

# mIMG = pygame.image.load("monkey.png")
# monkey = Button(screen, mIMG, 0.3, 500, 300)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
#     if monkey.draw():
#         screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
#         monkey.rect.center = (random.randint(50, 950),random.randint(50,550))

#     pygame.display.update()
#     clock.tick(60)


"""
Homework
For homework, I want you to come up with at least 3 ideas
for a final project. Try to come up with ideas that use some
of the topics we've learned in python 3 like Text, Players,
Buttons, keystate, mouse position, collision, and anything
else you want. Try to write some info on what you want to have
in the game.
Good Luck!

1.
-
2.
-
3.
-

"""

https://prod.liveshare.vsengsaas.visualstudio.com/join?4234F19552536F8F3AF121C2A438EF2309F7