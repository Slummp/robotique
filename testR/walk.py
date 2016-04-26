import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from inverse_kinematics import leg_ik
import sys
import signal

global robot

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
        hDiff = 10
        step = 70
        
        timeStep = 0.3
        initRobot(hBase)
        
        
        while 1:
            time.sleep(timeStep)
            
            # Lever les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase, 0, hBase + hDiff)
            moveLeg(robot.leg3, xBase, 0, hBase + hDiff)
            moveLeg(robot.leg5, xBase, 0, hBase + hDiff)

            # Avancer les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase - step, 0, hBase + hDiff)
            moveLeg(robot.leg3, xBase, -step, hBase + hDiff)
            moveLeg(robot.leg5, xBase, step, hBase + hDiff)
            
            # Avancer les pattes 2, 4, 6
            moveLeg(robot.leg2, xBase, step, hBase)
            moveLeg(robot.leg4, xBase - step, 0, hBase)
            moveLeg(robot.leg6, xBase, -step, hBase)
            
            time.sleep(timeStep)
            
            # Baisser les pattes 1, 3, 5
            moveLeg(robot.leg1, xBase - step, 0, hBase - hDiff)
            moveLeg(robot.leg3, xBase, -step, hBase - hDiff)
            moveLeg(robot.leg5, xBase, step, hBase - hDiff)
            
            time.sleep(timeStep)
            
            # Rappatrier les pattes 2, 4, 6
            moveLeg(robot.leg2, xBase, 0, hBase)
            moveLeg(robot.leg4, xBase, 0, hBase)
            moveLeg(robot.leg6, xBase, 0, hBase)
            
            # Reposer les autres pattes
            moveLeg(robot.leg1, xBase, 0, hBase)
            moveLeg(robot.leg3, xBase, 0, hBase)
            moveLeg(robot.leg5, xBase, 0, hBase)
            
