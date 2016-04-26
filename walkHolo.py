import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from inverse_kinematics import leg_ik
from math import cos, sin
import sys
import signal

global robot

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

def moveOn(angle = 0, step = 50, hBase = -80, hDiff = 30, timeStep = 0.3):
        stepX = cos(angle) * step
        stepY = sin(angle) * step
	
	time.sleep(timeStep)

	# Lever les pattes 1, 3, 5
	moveLeg(robot.leg1, 100, 0, hBase + hDiff)
	moveLeg(robot.leg3, 80, -80, hBase + hDiff)
	moveLeg(robot.leg5, 80, 80, hBase + hDiff)

	# Avancer les pattes 1, 3, 5
	moveLeg(robot.leg1, 100 + stepX, stepY, hBase + hDiff)      #(+stepX, +stepY, 0)  - 1
	moveLeg(robot.leg3, 80 - stepY, stepX - 80, hBase + hDiff)  #(-stepY, +stepX, 0)  - 3
	moveLeg(robot.leg5, 80 + stepY, -stepX + 80, hBase + hDiff) #(+stepY, -stepX, 0)  - 5

	# Avancer les pattes 2, 4, 6
	moveLeg(robot.leg4, 100 + stepX, stepY, hBase)              #(+stepX, +stepY, 0)  - 4
	moveLeg(robot.leg2, 80 + stepY, -stepX + 80, hBase)         #(+stepY, -stepX, 0)  - 2
	moveLeg(robot.leg6, 80 - stepY, stepX - 80, hBase)          #(-stepY, +stepX, 0)  - 6

	time.sleep(timeStep)

	# Avancer les pattes 1, 3, 5
	moveLeg(robot.leg1, 100 + stepX, stepY, hBase - hDiff)      #(+stepX, +stepY, 0)  - 1
	moveLeg(robot.leg3, 80 - stepY, stepX - 80, hBase - hDiff)  #(-stepY, +stepX, 0)  - 3
	moveLeg(robot.leg5, 80 + stepY, -stepX + 80, hBase - hDiff) #(+stepY, -stepX, 0)  - 5

	time.sleep(timeStep)

	# Rappatrier les pattes 2, 4, 6
	moveLeg(robot.leg4, 100, 0, hBase)
	moveLeg(robot.leg2, 80, 80, hBase)
	moveLeg(robot.leg6, 80, -80, hBase)

	# Reposer les autres pattes
	moveLeg(robot.leg1, 100, 0, hBase)
	moveLeg(robot.leg3, 80, -80, hBase)
	moveLeg(robot.leg5, 80, 80, hBase)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        print robot
        for m in robot.motors:
            print(m, m.present_position)
        for motor in robot.motors:
            motor.compliant = False

	initRobot(-80)
	while 1:
            moveOn(3.14/2)



