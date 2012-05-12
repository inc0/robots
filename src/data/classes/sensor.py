# -*- coding: utf-8 -*-
import pygame, sys,os
from pygame.locals import *
import settings

class Sensor():

    def __init__(self, angle, num_sensors, walls):

        self.angle = angle

        y_pos = 70+(40*num_sensors)

        self.position = (820, y_pos)

        self.image = pygame.Surface((160, 20))
        self.image.fill((0,0,0))

        self.rect = self.image.get_rect()
        self.rect.topleft = self.position

        fontFile = os.path.join(os.path.abspath(""),"data","media","fonts","cipher.ttf")
        self.font = pygame.font.Font(fontFile, 13)

        self.walls = walls

    def readValues(self, position, angle):




        self.value = str(int(position[0]))+" "+str(int(position[1]))+" "+str(int(angle+self.angle)%360)+"'"

    def input(self, events):
        pass

    def update(self, display):
        display.blit(self.image, self.position)

        text = self.font.render(self.value, True, (58,232, 0), (0, 0, 0))

        textRect = text.get_rect()

        textRect.centerx = self.position[0] + 80
        textRect.centery = self.position[1] + 10

        display.blit(text, textRect)