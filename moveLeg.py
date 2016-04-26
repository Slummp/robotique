import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from inverse_kinematics import leg_ik
import sys
import signal

robot = pypot.robot.from_json("robotConfig.json")

def moveLeg(leg, x, y, z, d=0.3):
    motors = [m.name for m in leg]
    print(leg)
    cmd = dict(zip(motors, leg_ik(x,y,z)))    
    robot.goto_position(cmd, d)

moveLeg(robot.leg1, 100, 20, 100)
time.sleep(1)
