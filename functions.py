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
    
