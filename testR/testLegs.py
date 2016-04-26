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

def moveLeg(leg, x, y, z, d=0.3):
    motors = [m.name for m in leg]
    print(leg)
    cmd = dict(zip(motors, leg_ik(x,y,z)))    
    robot.goto_position(cmd, d)
    

def initRobot(hBase, sleep):
    print("Leg 1")
    moveLeg(robot.leg1, 100, 0, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg1, 100, 0, hBase)
    time.sleep(sleep)

    print("Leg 2")
    moveLeg(robot.leg2, 80, 80, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg2, 80, 80, hBase)
    time.sleep(sleep)

    print("Leg 3")
    moveLeg(robot.leg3, 80, -80, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg3, 80, -80, hBase)
    time.sleep(sleep)

    print("Leg 4")
    moveLeg(robot.leg4, 100, 0, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg4, 100, 0, hBase)
    time.sleep(sleep)

    print("Leg 5")
    moveLeg(robot.leg5, 80, 80, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg5, 80, 80, hBase)
    time.sleep(sleep)

    print("Leg 6")
    moveLeg(robot.leg6, 80, -80, hBase + 20)
    time.sleep(sleep)

    moveLeg(robot.leg6, 80, -80, hBase)
    time.sleep(sleep)

def signal_handler(signal, frame):
    print "Shutting down..."
    time.sleep(0.5)
    initRobot(-100)
    time.sleep(0.5)
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        print robot
        for m in robot.motors:
            print(m, m.present_position)
        for motor in robot.motors:
            motor.compliant = False
        initRobot(-80, 0.4)



