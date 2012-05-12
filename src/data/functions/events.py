import pygame, sys,os
from pygame.locals import *

def common_events(events):
    for event in events:
        if event.type == QUIT: 
            sys.exit(0)
    
    
    return True   