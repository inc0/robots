import pygame, sys,os
from pygame.locals import *
import settings
from data.classes.robot import Robot
from data.functions.events import common_events

class Render:
    
    entities = []
    
    def __init__(self):
        self.window = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('Almost Skynet')
        
        self.background = pygame.Surface((800, 600))
        self.background = self.background.convert()
        self.background.fill((245, 217, 172))
        self.window.blit(self.background, (0, 0))

        self.sidebar = pygame.Surface((200, 600))
        self.sidebar = self.sidebar.convert()
        self.sidebar.fill((174, 174, 174))
        self.window.blit(self.sidebar, (800, 0))


    def addEntity(self,entity):
        self.entities.append(entity)
    
    def update(self, events):
        common_events(events)

        self.background.fill((245, 217, 172))
        self.window.blit(self.background, (0, 0))

        self.sidebar.fill((174, 174, 174))
        self.window.blit(self.sidebar, (800, 0))

        for entity in self.entities:
            entity.input(events)
            entity.update(self.window)
            
        pygame.display.flip()