import numpy as np
import modern_robotics as mr
import math

pi = math.pi

# question 1
M = np.array([[    1,    0,    0, 3.73],
              [    0,    1,    0,    0],
              [    0,    0,    1, 2.73],
              [    0,    0,    0,    1]])
print("\nQuestion 1:\n", np.array2string(M, separator=',', suppress_small=True))

# question 2
Slist = np.array([[    0,    0,    1,    0,   -1,    0],
                  [    0,    1,    0,    0,    0,    1],
                  [    0,    1,    0,    1,    0, 2.73],
                  [    0,    1,    0,-0.73,    0, 3.73],
                  [    0,    0,    0,    0,    0,    1],
                  [    0,    0,    1,    0,    -3.73,0]]).T
print("\nQuestion 2:\n", np.array2string(Slist, separator=',', suppress_small=True))

# question 3
Blist = np.array([[    0,    0,    1,    0, 2.73,    0],
                  [    0,    1,    0, 2.73,    0,-2.73],
                  [    0,    1,    0, 3.73,    0,   -1],
                  [    0,    1,    0,    2,    0,    0],
                  [    0,    0,    0,    0,    0,    1],
                  [    0,    0,    1,    0,    0,    0]]).T
print("\nQuestion 3:\n", np.array2string(Blist, separator=',', suppress_small=True))

# question 4
thetalist_space = np.array([-pi/2, pi/2, pi/3, -pi/4, 1, pi/6])
MatSpace = mr.FKinSpace(M, Slist, thetalist_space)
MatSpaceOff = np.around(MatSpace, decimals=2)
print("\nQuestion 4:\n", np.array2string(MatSpaceOff, separator=',', suppress_small=True))

# question 5
thetalist_body = np.array([-pi/2, pi/2, pi/3, -pi/4, 1, pi/6])
MatBody = mr.FKinBody(M, Blist, thetalist_body)
MatBodyOff = np.around(MatBody, decimals=2)
print("\nQuestion 5:\n", np.array2string(MatBodyOff, separator=',', suppress_small=True))
