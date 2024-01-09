#TACE Final culminating
#This game is liverpool jeopardy

import pygame
import sys

Boxinfo2 = [[20, 330, "CP1.png"]]
Boxinfo = [[20, 350, "CP1.png"], [20,450,"CP2.png"],[20,550,"CP3.png"],[20,650,"CP4.png"],[20,750,"CP5.png"]]
          # [20,10,"CP1.png"],[20,20,"CP2.png"],[20,30,"CP3.png"],[20,40,"CP4.png"],[20,50,"CP5.png"]]

class BOX:
    def __init__(self, x,y,filename):
        self.x = x
        self.y = y
        self.size = (200, 100)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

#main
win = pygame.display.set_mode((1100, 900))
size=(1100,900)

Background = pygame.image.load("Background.jpg")
Background = pygame.transform.scale(Background,size)
BackgroundRect = Background.get_rect()

#make boxes
#BOX1=BOX(0, 50, "CP1.png")

# list of box objects
Board=[]
for i in range(len(Boxinfo)):
    newBox = BOX(Boxinfo[i][0], Boxinfo[i][1], Boxinfo[i][2])
    Board.append  (newBox)

#Box1 = BOX(10, 50, "CP1.PNG")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    win.blit(Background, BackgroundRect)
    for i in range(len(Board)):
        win.blit(Board[i].image, Board[i].rect)
 #   win.blit(Box1.image, Box1.rect)
    pygame.display.update()
