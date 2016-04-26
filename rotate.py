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
def signal_handler(signal, frame):
    print "Shutting down..."
    time.sleep(1)
    initRobot(-100)
    time.sleep(1)
    sys.exit(0)
###############################################################

global robot
###############################################################
# Fonctions du robot
def moveLeg(leg, x, y, z, d=0.5):
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
        xBase = 80
        yBase = 80
        hDiff = 30
        step = -70
        
        timeStep = 0.3

        
        initRobot(hBase)
        
        while 1:
            # Lever les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase, 0, hBase + hDiff)
            moveLeg(robot.leg3, xBase, -yBase, hBase + hDiff)
            moveLeg(robot.leg5, xBase, yBase, hBase + hDiff)
            
            time.sleep(timeStep)

            # Rappatrier les pattes 2, 4, 6
            moveLeg(robot.leg4, xBase, 0, hBase)
            moveLeg(robot.leg6, xBase, -yBase, hBase)
            moveLeg(robot.leg2, xBase, yBase, hBase)

            # Tourner les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase, step, hBase + hDiff)
            moveLeg(robot.leg3, xBase, -yBase + step, hBase + hDiff)
            moveLeg(robot.leg5, xBase, yBase + step, hBase + hDiff)
            
            time.sleep(timeStep)

            # Baisser les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase, step, hBase)
            moveLeg(robot.leg3, xBase, -yBase + step, hBase)
            moveLeg(robot.leg5, xBase, yBase + step, hBase)
            
            time.sleep(timeStep)
            
            # Lever les pattes 2, 4, 6
            moveLeg(robot.leg4, xBase, 0, hBase + hDiff)
            moveLeg(robot.leg6, xBase, -yBase, hBase + hDiff)
            moveLeg(robot.leg2, xBase, yBase, hBase + hDiff)
            
            time.sleep(timeStep)

            # Rappatrier les pattes 1, 3, 6
            moveLeg(robot.leg1, xBase, 0, hBase)
            moveLeg(robot.leg3, xBase, -yBase, hBase)
            moveLeg(robot.leg5, xBase, yBase, hBase)

            # Tourner les pattes 2, 4, 6
            moveLeg(robot.leg4, xBase, step, hBase + hDiff)
            moveLeg(robot.leg6, xBase, -yBase + step, hBase + hDiff)
            moveLeg(robot.leg2, xBase, yBase + step, hBase + hDiff)
            
            time.sleep(timeStep)

            # Baisser les pattes 2, 4, 6
            moveLeg(robot.leg4, xBase, step, hBase)
            moveLeg(robot.leg6, xBase, -yBase + step, hBase)
            moveLeg(robot.leg2, xBase, yBase + step, hBase)
            
            time.sleep(timeStep)
        
        initRobot(hBase)
        
