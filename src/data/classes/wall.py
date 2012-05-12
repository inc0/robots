import pygame, sys,os
from pygame.locals import *
import settings
from data.functions.events import common_events


class Wall(pygame.sprite.Sprite):
    
    def __init__(self, position, metrics):
        pygame.sprite.Sprite.__init__(self)
        
        self.metrics = metrics
        self.position = position
        
        self.image = pygame.Surface(self.metrics)
        self.image.fill((0,0,255))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        
    def input(self, events):
        pass
        
    def update(self, display):
        display.blit(self.image, self.position)