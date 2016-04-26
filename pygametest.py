#!/usr/bin/python
import pygame
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((500, 500))
continuer = 1
moving = 0
pygame.draw.circle(window, [25, 25, 200] ,coord,5,0)
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            moving = 1
        if event.type == MOUSEBUTTONUP and event.button == 1:
            moving = 0
        if event.type == MOUSEMOTION and moving:
            print(event.pos)

