import pygame
from pygame.locals import *
import sys
from itertools import cycle

SCREENWIDTH = 822
SCREENHEIGHT = 199
FPS = 30

class MyMap():

    def __init__(self, x, y):
        self.bg = pygame.image.load("marie_adventure\\image\\bg.png").convert_alpha()
        self.x = x
        self.y = y
    
    def map_rolling(self):
        if self.x < -800:
            self.x = 800
        else:
            self.x -= 5
    
    def map_update(self):
        SCREEN.blit(self.bg, (self.x, self.y))


class Marie():
    
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.jumpState = False
        self.jumpHeight = 130
        self.lowest_y = 140
        self.jumpValue = 0

        self.marieIndex = 0
        self.marieIndexGen = cycle([0,1,2])

        self.adventure_img = (
            pygame.image.load("marie_adventure\\image\\adventure1.png").convert_alpha(),
            pygame.image.load("marie_adventure\\image\\adventure2.png").convert_alpha(),
            pygame.image.load("marie_adventure\\image\\adventure3.png").convert_alpha(),
        )

        self.jump_audio = pygame.mixer.Sound("marie_adventure\\audio\\jump.wav")
        self.rect.size = self.adventure_img[0].get_size()
        self.x = 50
        self.y = self.lowest_y
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.jumpState = True

    def move(self):
        if self.jumpState:
            if self.rect.y >= self.lowest_y:
                self.jumpValue = -5
            if self.rect.y <= self.lowest_y - self.jumpHeight:
                self.jumpValue = 5
            self.rect.y += self.jumpValue
            if self.rect.y >= self.lowest_y:
                self.jumpState = False
    
    def draw_marie(self):
        marieIndex = next(self.marieIndexGen)
        SCREEN.blit(self.adventure_img[marieIndex], (self.x, self.rect.y))



def mainGame():
    score = 0
    over = False
    
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    SCREEN = pygame.display.set_mode( (SCREENWIDTH, SCREENHEIGHT) )
    pygame.display.set_caption('玛丽冒险')

    bg1 = MyMap(0, 0)
    bg2 = MyMap(800, 0)

    marie = Marie()

    while True:
        if over==False:
            bg1.map_update()
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()
            marie.move()
            marie.draw_marie()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN and event.key == K_SPACE:
                if marie.rect.y >= marie.lowest_y:
                    marie.jump_audio.play()
                    marie.jump()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    mainGame()