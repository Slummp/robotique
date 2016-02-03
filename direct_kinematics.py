# Alexandre Brouste et Benjamin Bordel

from math import *

def leg_dk(theta1, theta2, theta3, l1 = 51, l2 = 63.7, l3 = 93):
    theta1 = radians(theta1)
    theta2 = radians(theta2)
    theta3 = radians(theta3)

    alpha = radians(20.69)
    beta = radians(5.06)

    # newTheta2 = theta2 - alpha
    # newTheta3 = theta3 + beta

    newTheta2 = theta2 + alpha
    newTheta3 = alpha + (pi / 2) + theta3 + beta

    P1 = {
        "x": cos(theta1) * l1,
        "y": sin(theta1) * l1,
        "z": 0
    }

    P2 = {
        "x": P1["x"] + cos(theta1) * cos(newTheta2) * l2,
        "y": P1["y"] + sin(theta1) * cos(newTheta2) * l2,
        "z": P1["z"] + sin(newTheta2) * l2
    }

    P3 = {
        "x": P2["x"] + cos(theta1) * cos(newTheta2 + newTheta3) * l3,
        "y": P2["y"] + sin(theta1) * cos(newTheta2 + newTheta3) * l3,
        "z": P2["z"] + sin(newTheta2 + newTheta3) * l3
    }

    print("P1 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**P1))
    print("P2 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**P2))
    print("P3 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**P3))