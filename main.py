#TACE Final culminating
#This game is liverpool jeopardy

#TACE Final culminating
#This game is liverpool jeopardy

import pygame
import sys
import random


Boxinfo2 = [[20, 330, "CP1.png"]]
Boxinfo = [[20, 300, "CP1.png"], [20,450,"CP2.png"],[20,580,"CP3.png"],[20,700,"CP4.png"],[20,820,"CP5.png"],
[300,300,"CP1.png"],[300,450,"CP2.png"],[300,580,"CP3.png"],[300,700,"CP4.png"],[300,820,"CP5.png"],
[600,300,"CP1.png"],[600,450,"CP2.png"],[600,580,"CP3.png"],[600,700,"CP4.png"],[600,820,"CP5.png"],
[870,300,"CP1.png"],[870,450,"CP2.png"],[870,580,"CP3.png"],[870,700,"CP4.png"],[870,820,"CP5.png"]]
white = (255,255,255)
rect_size = 20
class BOX:
    def __init__(self, x,y,filename):
        self.x = x
        self.y = y
        self.size = (200, 100)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x, self.y)

    def checkCollision(self, sprite1):
        col=self.rect.colliderect(sprite1)
        if col == True:

            return True
class TextBox:
    def __init__(self, x, y, width, height, font_size=32):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.Font(None, font_size)
        self.color = black
        self.active = False

    def checkCollision(self, sprite1):
        col = self.rect.colliderect(sprite1)
        if col == BOX:
            self.active= True
            TextBox.render(500,400)
        else:
            self.active=False
            return True






def readQuestions():
    questions = []

    with open("C1.txt") as file:
        questions = [line.rstrip("\n") for line in file]

    # remove empty lines

    questions = [x for x in questions if x != '']

    file.close()

    return(questions[(random.randint(0, len(questions) - 1))])


def displayQuestion(win, question):
    text = font.render(question, True, green, blue)
    textRect = text.get_rect()
    textRect.center = (textX // 2, textY // 2)
    while True:
        win.fill(white)
        win.blit(text, textRect)
        pygame.display.update()
index=[]
def identify(win, Boxinfo):
    Boxinfo.index(index)
    Answer = font.render(question, True, green, blue)
    AnswerRect = Answer.get_rect()
    AnswerRect.center = (textX // 2, textY // 2)

    while True:
        win.fill(white)
        win.blit(Answer, AnswerRect)
        pygame.display.update()

#main
pygame.init()
win = pygame.display.set_mode((1100, 900))
size=(1100,900)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
textX = 400
textY = 400
font = pygame.font.Font('freesansbold.ttf', 32)


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
chosen=False

while chosen== False:

    mouse_pos=pygame.mouse.get_pos()
    mouseRect=pygame.draw.rect(win,white,[mouse_pos[0],mouse_pos[1],rect_size, rect_size])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    win.blit(Background, BackgroundRect)
    for i in range(len(Board)):
        if pygame.mouse.get_pressed()[0]:
            if Board[i].checkCollision(mouseRect):
                chosen=True

                question = readQuestions()
                displayQuestion(win,question)


        win.blit(Board[i].image, Board[i].rect)


 #   win.blit(Box1.image, Box1.rect)
    pygame.display.update()


