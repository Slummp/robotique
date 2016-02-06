# Alexandre Brouste et Benjamin Bordel

from functions import *


def leg_ik(x, y, z, l1=51, l2=63.7, l3=93):
    alpha = radians(20.69)
    beta = radians(5.06)

    #

    l_proj = pythagore(x, y)

    d13 = l_proj - l1

    d = pythagore(d13, z)

    a = asin(z / d)

    b = inverse_al_kashi(l3, l2, d)

    #

    theta1 = atan2(y, x)

    theta21 = - a - b - alpha
    # theta22 = - a + b - alpha

    theta31 = inverse_al_kashi(d, l2, l3) - (pi / 2) - alpha - beta
    # theta32 = inverse_al_kashi(d, l2, l3) + (pi / 2) - alpha - beta

    # print "l_proj = %.2f ; d13 = %.2f ; d = %.2f ; a = %.2f ; b = %.2f" % (l_proj, d13, d, degrees(a), degrees(b))

    print "Theta 1 = %.2f ; Theta 2 = %.2f ; Theta 3 = %.2f" % (degrees(theta1), degrees(theta21), degrees(theta31))
