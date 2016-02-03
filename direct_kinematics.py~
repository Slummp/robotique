import math

def leg_dk(theta1, theta2, theta3, l1 = 51, l2 = 63.7, l3 = 93):
  theta1 = math.radians(theta1)
  theta2 = math.radians(theta2)
  theta3 = math.radians(theta3)

  alpha = math.radians(20.69)
  beta = math.radians(5.06)
  
  d12 = l2 * math.cos(alpha) * math.cos(theta2)
  d23 = l3 * math.cos(beta) * math.cos(theta2 + theta3)

  x = (l1 + math.cos(alpha) * l2 * math.cos(theta2) + math.sin(theta2) * math.sin(alpha) * l2 + math.sin(theta2) * math.cos(beta) * l3 + math.cos(theta2) * math.sin(beta) * l3) * math.cos(theta1)

  y = (l1 + math.cos(alpha) * l2 * math.cos(theta2) + math.sin(theta2) * math.sin(alpha) * l2 + math.sin(theta2) * math.cos(beta) * l3 + math.cos(theta2) * math.sin(beta) * l3) * math.sin(theta1)

  z = math.cos(alpha) * l2 * math.sin(theta2) - math.cos(theta2) * math.sin(alpha) * l2 - math.cos(theta2) * math.cos(beta) * l3 + math.sin(theta2) * math.sin(beta) * l3

  print("t1 = %.2f, t2 = %.2f, t3 = %.2f\nx = %.2f, y = %.2f et z = %.2f" % (theta1, theta2, theta3, x, y, z))
