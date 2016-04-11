#!/usr/bin/python
import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from inverse_kinematics import leg_ik
import sys
import signal
from functions import *

###############################################################
# Init Pygame
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 500))
continuer = 1
moving = 0
pygame.draw.circle(window, [25, 25, 200] ,(250,250),5,0)
pygame.display.flip()
###############################################################

global robot
###############################################################
# Fonctions du robot
def moveLeg(leg, x, y, z, d=0.0):
    motors = [m.name for m in leg]
    cmd = dict(zip(motors, leg_ik(x,y,z)))    
    robot.goto_position(cmd, d)
    

def initRobot(hBase):
    moveLeg(robot.leg1, 100, 0, hBase)
    moveLeg(robot.leg2, 100, 0, hBase)
    moveLeg(robot.leg3, 100, 0, hBase)
    moveLeg(robot.leg4, 100, 0, hBase)
    moveLeg(robot.leg5, 100, 0, hBase)
    moveLeg(robot.leg6, 100, 0, hBase)

def moveCenter(x, y, hBase):
    # Deplacer toutes les pattes
    moveLeg(robot.leg1, -x + xBase, -y, hBase)

    moveLeg(robot.leg4, x + xBase, y, hBase)



    moveLeg(robot.leg2, x + xBase, -y, hBase)
    moveLeg(robot.leg3, x + xBase, -y, hBase)

    moveLeg(robot.leg5, -x + xBase, y, hBase)
    moveLeg(robot.leg6, -x + xBase, y, hBase)
###############################################################


if __name__ == '__main__':
    
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        print robot
        for m in robot.motors:
            print(m, m.present_position)
        for motor in robot.motors:
            motor.compliant = False
        
        hBase = -100
        xBase = 100
        initRobot(hBase)
        
        time.sleep(1)
        
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = 0
                    
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    moving = 1
                    
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    moving = 0
                    
                if event.type == MOUSEMOTION and moving:
                    x = (event.pos[0]-250) / 5
                    y = (event.pos[1]-250) / 5
                    
                    print("SE DEPLACE ", x, y)
                    
                    moveCenter(x, y, hBase)
                    
                    pygame.draw.circle(window, [abs(x)*5,abs(y)*5,abs(x)*2 + abs(y)*2] ,(event.pos[0],event.pos[1]),10,0)
                    pygame.display.flip()
                time.sleep(0.0025)
        initRobot(hBase)
        
