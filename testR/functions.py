# Alexandre Brouste et Benjamin Bordel

from math import *


def pythagore(side1, side2):
    return sqrt(side1**2 + side2**2)


def inverse_pythagore(hypotenuse, side):
    return sqrt(hypotenuse**2 - side**2)


def opposite_from_sine(angle, hypotenuse):
    return sin(angle) * hypotenuse


def hypotenuse_from_sine(angle, opposite):
    return opposite / sin(angle)


def adjacent_from_cosine(angle, hypotenuse):
    return cos(angle) * hypotenuse


def hypotenuse_from_cosine(angle, adjacent):
    return adjacent / cos(angle)


def opposite_from_tangent(angle, adjacent):
    return tan(angle) * adjacent


def adjacent_from_tangent(angle, opposite):
    return opposite / tan(angle)


def al_kashi(angle, side1, side2):
    return sqrt(side1**2 + side2**2 - 2 * side1 * side2 * cos(angle))


def inverse_al_kashi(opposite, side1, side2):
    return acos((side1**2 + side2**2 - opposite**2) / (2 * side1 * side2))


def moveLeg(leg, x, y, z, d=0.2):
    motors = [m.name for m in leg]
    print(leg)
    cmd = dict(zip(motors, leg_ik(x,y,z)))    
    robot.goto_position(cmd, d)


def signal_handler(signal, frame):
    print "Shutting down..."
    time.sleep(1)
    initRobot(-100)
    time.sleep(1)
    sys.exit(0)
    

def initRobot(hBase):
    moveLeg(robot.leg1, 100, 0, hBase)
    moveLeg(robot.leg2, 100, 0, hBase)
    moveLeg(robot.leg3, 100, 0, hBase)
    moveLeg(robot.leg4, 100, 0, hBase)
    moveLeg(robot.leg5, 100, 0, hBase)
    moveLeg(robot.leg6, 100, 0, hBase)
