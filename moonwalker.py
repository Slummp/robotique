import itertools
import time
import numpy
import pypot.robot
from contextlib import closing
import pypot.primitive


if __name__ == '__main__':
    with closing(pypot.robot.from_json("robotConfig.json")) as robot:
        print robot
        for m in robot.motors:
            print(m, m.present_position)
        for motor in robot.motors:
            motor.compliant = False
        motors = [m.name for m in robot.leg1]
        
        cmd = dict(zip(motors, [20,20,20]))
        robot.goto_position(cmd, 0)
