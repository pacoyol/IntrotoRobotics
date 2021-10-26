#!/usr/bin/env python
import numpy as np
from scipy.linalg import expm

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""


def Get_MS():
    # =================== Your code starts here ====================#
    # Fill in the correct values for S1~6, as well as the M matrix

    S_1 = np.array([[0, -1, 0, 0],
                    [1, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])

    S_2 = np.array([[0, 0, 0, 0],
                    [0, 0, -1, 2],
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]])

    S_3 = np.array([[0, 0, 0, 0],
                    [0, 0, 0, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]])

    S = [S_1, S_2, S_3]

    M = np.array([[-1, 0, 0, 0],
                  [0, 0, 1, 3],
                  [0, 1, 0, 2],
                  [0, 0, 0, 1]])
    # ==============================================================#
    return M, S


"""
Function that calculates encoder numbers for each motor
"""

M, S = Get_MS()

theta = [np.pi/2, np.pi/2, 1]

mat_temp = np.eye(4)

for i in range(3):
    mat_temp = np.matmul(mat_temp, expm(S[i] * theta[i]))

T = mat_temp.dot(M)
print(T)
# print(mat_temp)
# T1 = np.matmul(M, mat_temp)
print(T1)