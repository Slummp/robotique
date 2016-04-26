#!/bin/py
import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from inverse_kinematics import leg_ik
from math import *
import sys
import signal
global robot
###############################################################
# Init Pygame
import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 500))
continuer = 1

pygame.display.flip()
###############################################################

###############################################################
# Fonctions du robot
def moveLeg(leg, x, y, z, d=0.3):
    motors = [m.name for m in leg]
    print(leg)
    cmd = dict(zip(motors, leg_ik(x,y,z)))    
    robot.goto_position(cmd, d)
    

def initRobot(hBase):
    moveLeg(robot.leg1, 100, 0, hBase)
    moveLeg(robot.leg2, 80, 80, hBase)
    moveLeg(robot.leg3, 80, -80, hBase)
    moveLeg(robot.leg4, 100, 0, hBase)
    moveLeg(robot.leg5, 80, 80, hBase)
    moveLeg(robot.leg6, 80, -80, hBase)

def signal_handler(signal, frame):
    print "Shutting down..."
    time.sleep(0.5)
    initRobot(-100)
    time.sleep(0.5)
    sys.exit(0)

def moveOn(d = 0.3, angle = 0, step = 40, hBase = -80, hDiff = 30):
        stepX = cos(angle) * step
        stepY = sin(angle) * step
	
        timeStep = d
	time.sleep(timeStep)

	# Lever les pattes 1, 3, 5
	moveLeg(robot.leg1, 100, 0, hBase + hDiff, d)
	moveLeg(robot.leg3, 80, -80, hBase + hDiff, d)
	moveLeg(robot.leg5, 80, 80, hBase + hDiff, d)

	# Avancer les pattes 1, 3, 5
	moveLeg(robot.leg1, 100 + stepX, stepY, hBase + hDiff, d)      #(+stepX, +stepY, 0)  - 1
	moveLeg(robot.leg3, 80 - stepY, stepX - 80, hBase + hDiff, d)  #(-stepY, +stepX, 0)  - 3
	moveLeg(robot.leg5, 80 + stepY, -stepX + 80, hBase + hDiff, d) #(+stepY, -stepX, 0)  - 5

	# Avancer les pattes 2, 4, 6
	moveLeg(robot.leg4, 100 + stepX, stepY, hBase, d)              #(+stepX, +stepY, 0)  - 4
	moveLeg(robot.leg2, 80 + stepY, -stepX + 80, hBase, d)         #(+stepY, -stepX, 0)  - 2
	moveLeg(robot.leg6, 80 - stepY, stepX - 80, hBase, d)          #(-stepY, +stepX, 0)  - 6

	time.sleep(timeStep)

	# Avancer les pattes 1, 3, 5
	moveLeg(robot.leg1, 100 + stepX, stepY, hBase - hDiff, d)      #(+stepX, +stepY, 0)  - 1
        print(80 - stepY, stepX - 80, hBase - hDiff, d)
	moveLeg(robot.leg3, 80 - stepY, stepX - 80, hBase - hDiff, d)  #(-stepY, +stepX, 0)  - 3
	moveLeg(robot.leg5, 80 + stepY, -stepX + 80, hBase - hDiff, d) #(+stepY, -stepX, 0)  - 5

	time.sleep(timeStep)

	# Rappatrier les pattes 2, 4, 6
	moveLeg(robot.leg4, 100, 0, hBase, d)
	moveLeg(robot.leg2, 80, 80, hBase, d)
	moveLeg(robot.leg6, 80, -80, hBase, d)

	# Reposer les autres pattes
	moveLeg(robot.leg1, 100, 0, hBase, d)
	moveLeg(robot.leg3, 80, -80, hBase, d)
	moveLeg(robot.leg5, 80, 80, hBase, d)
###############################################################
# Windows

def reDisplay(red, d = '-', x = 0, y = 0):
	font = pygame.font.Font(None, 36)
	window.fill((0,0,0))
	pygame.draw.circle(window, [60, 60, 200] ,(250,250),250,0)
	pygame.draw.circle(window, [(255 if red else 25), 25, 200] ,(250,250),5,0)
	text = font.render(str(d), 1, (255, 255, 255))
        window.blit(text, (0,0))
	pygame.draw.line(window, (25, 60, 40), (250, 250), (x, y), 1)
	pygame.display.flip()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    reDisplay(0)
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        print robot
        for m in robot.motors:
            print(m, m.present_position)
        for motor in robot.motors:
            motor.compliant = False
        
	
	initRobot(-80)
        theta = 0
        distance = 0.3
        x = y = 0

	while continuer:
            event = pygame.event.poll()
            if event.type == QUIT:
		    signal_handler(0,0)
                    continuer = 0
	    xMouse = pygame.mouse.get_pos()[0]
	    yMouse = pygame.mouse.get_pos()[1]
            if xMouse != x or yMouse != y:
                    x = (250-xMouse)
                    y = (250-yMouse)
                    theta = atan2(x, y)
                    distance = (250 - sqrt(x ** 2 + y ** 2))**2 / 62500 * 1.7 + 0.3
                    if (distance < 0.3):
                      distance = 0.3
                    
            if (distance < 1.7):
                moveOn(distance, theta)
		reDisplay(1, distance, xMouse, yMouse)
            else:
		reDisplay(0, distance)

