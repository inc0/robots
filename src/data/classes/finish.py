import pygame, sys,os
from pygame.locals import *
import settings
from data.functions.events import common_events


class Finish(pygame.sprite.Sprite):
    
    player = None;
    
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        
        self.image = pygame.Surface((40,40))
        self.image.fill((10,255,10))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        
    def input(self, events):
        pass
        
    def update(self, display):
        display.blit(self.image, self.position)
        
        collide = pygame.sprite.spritecollide(self, self.player, False)
        if(collide):
             sys.exit(0)