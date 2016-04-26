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

        coord = (10, 10)

        x = coord[0]
        y = coord[1]
        
        timeStep = 0.3
        initRobot(hBase)
        
        # Déplacer toutes les pattes
        moveLeg(robot.leg1, x, y, hBase)

        moveLeg(robot.leg4, -x, -y, hBase)



        moveLeg(robot.leg2, x, -y, hBase)
        moveLeg(robot.leg3, x, -y, hBase)

        moveLeg(robot.leg5, -x, y, hBase)
        moveLeg(robot.leg6, -x, y, hBase)
