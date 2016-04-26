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
pygame.draw.circle(window, [60, 60, 200] ,(250,250),250,0)
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
    moveLeg(robot.leg2, 80, 80, hBase)
    moveLeg(robot.leg3, 80, -80, hBase)
    moveLeg(robot.leg4, 100, 0, hBase)
    moveLeg(robot.leg5, 80, 80, hBase)
    moveLeg(robot.leg6, 80, -80, hBase)

def moveCenter(x, y, hBase, d = 0.3):
    # Deplacer toutes les pattes
    moveLeg(robot.leg1, -y + 100, -x, hBase, d)

    moveLeg(robot.leg4, y + 100, x, hBase, d)



    moveLeg(robot.leg2, x + 80, -y + 80, hBase, d)
    moveLeg(robot.leg3, x + 80, -y - 80, hBase, d)

    moveLeg(robot.leg5, -x + 80, y + 80, hBase, d)
    moveLeg(robot.leg6, -x + 80, y - 80, hBase, d)
def signal_handler(signal, frame):
    print "Shutting down..."
    time.sleep(0.5)
    initRobot(-100)
    time.sleep(0.5)
    sys.exit(0)
###############################################################


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
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
		    signal_handler(0,0)
                    continuer = 0
                    
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    moving = 1
                    
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    moving = 0
                    
                if event.type == MOUSEMOTION and moving:
                    x = (event.pos[0]-250) / 5
                    y = (event.pos[1]-250) / 5
                    distance = ( sqrt(x ** 2 + y ** 2))
                    if (distance < 50):
                    	moveCenter(x, y, hBase)
                    	pygame.draw.circle(window, [10,10,10] ,(event.pos[0],event.pos[1]),2,0)
                    pygame.display.flip()
                time.sleep(0.0025)
        initRobot(hBase)
        
