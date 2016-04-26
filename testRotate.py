#!/usr/bin/python
import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive
from direct_kinematics import leg_dk
import sys
import signal
from functions import *

global robot

if __name__ == '__main__':
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        leg_dk(robot.leg2[0].present_position, robot.leg2[1].present_position, robot.leg2[2].present_position)
        
        print("\n")
        
        leg_dk(robot.leg3[0].present_position, robot.leg3[1].present_position, robot.leg3[2].present_position)
