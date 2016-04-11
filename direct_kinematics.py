# Alexandre Brouste et Benjamin Bordel

from math import *


def leg_dk(theta1, theta2, theta3, l1=51, l2=63.7, l3=93):
    theta1 = radians(theta1)
    theta2 = -radians(theta2)
    theta3 = radians(theta3)

    alpha = radians(20.69)
    beta = radians(5.06)

    new_theta2 = theta2 - alpha
    new_theta3 = theta3 + beta + alpha - (pi / 2)

    p1 = {
        "x": cos(theta1) * l1,
        "y": sin(theta1) * l1,
        "z": 0
    }

    p2 = {
        "x": p1["x"] + cos(theta1) * cos(new_theta2) * l2,
        "y": p1["y"] + sin(theta1) * cos(new_theta2) * l2,
        "z": p1["z"] + sin(new_theta2) * l2
    }

    p3 = {
        "x": p2["x"] + cos(theta1) * cos(new_theta2 + new_theta3) * l3,
        "y": p2["y"] + sin(theta1) * cos(new_theta2 + new_theta3) * l3,
        "z": p2["z"] + sin(new_theta2 + new_theta3) * l3
    }

    #print("P1 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**p1))
    #print("P2 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**p2))
    print("P3 : x:{x:.2f} y:{y:.2f} z:{z:.2f}".format(**p3))
