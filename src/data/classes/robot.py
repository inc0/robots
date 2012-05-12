import pygame, sys,os
from pygame.locals import *
import settings
from data.functions.vector import calculate_shift



class Robot(pygame.sprite.Sprite):
    position = [0,0]
    moved = [0,0]
    walls = []
    angle = 0
    sensors = []

    def __init__(self, start_position):
        pygame.sprite.Sprite.__init__(self)
        image_file_name = os.path.join(os.path.abspath(""),"data","media","images","robot.bmp")

        self.oryginal_image = pygame.image.load(image_file_name)
        self.image = self.oryginal_image
        self.rect = self.image.get_rect()
        self.rect.topleft = start_position


        
    def update(self, display):
        self.position[0] = self.rect.topleft[0];
        self.position[1] = self.rect.topleft[1];
        
        newpos= [self.position[0], self.position[1]]
        
        newpos[0] += self.moved[0]
        newpos[1] += self.moved[1]
        
        self.moved = [0,0]
        
        self.rect.topleft = [newpos[0], self.position[1]]
        
        collide = pygame.sprite.spritecollide(self, self.walls, False)
        if(collide):
            self.rect.topleft = [self.position[0], self.position[1]]
        else:
            self.position[0] = newpos[0]
            
        self.rect.topleft = [self.position[0], newpos[1]]


        collide = pygame.sprite.spritecollide(self, self.walls, False)
        if(collide):
            self.rect.topleft = [self.position[0], self.position[1]]
        else:
            self.position[1] = newpos[1]

        for sensor in self.sensors:
            sensor.readValues(self.position, self.angle)
        
        display.blit(self.image, self.position)
        
    def move(self, direction):
        self.moved = calculate_shift(self.moved, self.angle, settings.MOVE_SPEED*direction)
        
    def rotate(self, deg):
        self.angle += deg*settings.ROTATE_SPEED
        self.image = pygame.transform.rotate(self.oryginal_image, self.angle*(-1))


    def input(self, events): 
        pressed = pygame.key.get_pressed()
        if(pressed[pygame.K_UP]):
            self.move(1)
        if(pressed[pygame.K_DOWN]):
            self.move(-1)
        if(pressed[pygame.K_LEFT]):
            self.rotate(-1)
        if(pressed[pygame.K_RIGHT]):
            self.rotate(1)




