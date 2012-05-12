import pygame, sys,os
from data.classes.robot import Robot
from data.classes.render import Render
from data.classes.wall import Wall
from data.classes.finish import Finish
from data.classes.clock import Clock
import time

pygame.init()

from labirynth import *

clock = pygame.time.Clock()

objFinish = Finish(finish_position)
objRobot = Robot(start_position)
objRender = Render()

objRobot.walls = walls
objRobot.sensors = sensors
objFinish.player = [objRobot]

objClock = Clock()

objRender.addEntity(objRobot)
objRender.addEntity(objFinish)
objRender.addEntity(objClock)

for sensor in sensors:
    objRender.addEntity(sensor)

for wall in walls:
    objRender.addEntity(wall)

pygame.mixer.init()
bgFile = os.path.join(os.path.abspath(""),"data","media","audio","bgm01.wav")
backgroundMusic = pygame.mixer.Sound(bgFile)
backgroundMusic.play()


while True:
   clock.tick(30)
   objRender.update(pygame.event.get())
   