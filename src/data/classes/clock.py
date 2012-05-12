import pygame, sys,os
from pygame.locals import *
import settings
import time

class Clock(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.position = (820, 20)

        self.image = pygame.Surface((160, 30))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        self.initialTime = time.time()

        fontFile = os.path.join(os.path.abspath(""),"data","media","fonts","cipher.ttf")
        self.font = pygame.font.Font(fontFile, 21)


    def input(self, events):
        pass

    def update(self, display):
        display.blit(self.image, self.position)

        gameTime = time.time() - self.initialTime

        


        text = self.font.render(str(int(gameTime)), True, (58,232, 0), (0, 0, 0))

        textRect = text.get_rect()

        textRect.centerx = self.position[0] + 80
        textRect.centery = self.position[1] + 15

        display.blit(text, textRect)