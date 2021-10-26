#!/usr/bin/env python
import numpy as np
from scipy.linalg import expm
import math
from lab4_header import *

"""
Use 'expm' for matrix exponential.
Angles are in radian, distance are in meters.
"""


def Get_MS():
    # =================== Your code starts here ====================#
    # Fill in the correct values for a1~6 and q1~6, as well as the M matrix
    # M = np.eye(4)
    # S = np.zeros((6,6))
    M = [[0, -1, 0, 390], [0, 0, -1, 401], [1, 0, 0, 215.5], [0, 0, 0, 1]]
    s1 = [0, 0, 1]
    s2 = [0, 1, 0]
    s3 = [0, 1, 0]
    s4 = [0, 1, 0]
    s5 = [1, 0, 0]
    s6 = [0, 1, 0]

    q1 = [-150, 150, 162]
    q2 = [-150, 270, 162]
    q3 = [94, 270, 162]
    q4 = [307, 177, 162]
    q5 = [307, 260, 162]
    q6 = [390, 260, 162]

    v1 = -1 * np.cross(s1, q1)
    v2 = -1 * np.cross(s2, q2)
    v3 = -1 * np.cross(s3, q3)
    v4 = -1 * np.cross(s4, q4)
    v5 = -1 * np.cross(s5, q5)
    v6 = -1 * np.cross(s6, q6)

    S = np.array([[s1, v1], [s2, v2], [s3, v3], [s4, v4], [s5, v5], [s6, v6]])
    # ==============================================================#
    return M, S


def box_screw(S):
    return np.matrix([[0, -S[0][2], S[0][1], S[1][0]],
                      [S[0][2], 0, -S[0][0], S[1][1]],
                      [-S[0][1], S[0][0], 0, S[1][2]],
                      [0, 0, 0, 0]])


"""

Function that calculates encoder numbers for each motor
"""


def lab_fk(theta1, theta2, theta3, theta4, theta5, theta6):
    # Initialize the return_value
    return_value = [None, None, None, None, None, None]

    print("Foward kinematics calculated:\n")

    # =================== Your code starts here ====================#
    thetas = np.array([theta1, theta2, theta3, theta4, theta5, theta6])
    T = np.eye(4)

    M, S = Get_MS()
    for i in range(6):
        T = np.matmul(T, expm(box_screw(S[i]) * thetas[i]))

    T = np.matmul(T, M)
    # ==============================================================#
    print(str(T) + "\n")
    return_value[0] = theta1 + PI
    return_value[1] = theta2
    return_value[2] = theta3
    return_value[3] = theta4 - (0.5 * PI)
    return_value[4] = theta5
    return_value[5] = theta6

    return return_value


"""
Function that calculates an elbow up Inverse Kinematic solution for the UR3
"""


def lab_invk(xWgrip, yWgrip, zWgrip, yaw_WgripDegree):
    # =================== Your code starts here ====================#
    L = [0, 152, 120, 244, 93, 213, 83, 83, 82, 53.5, 59]
    theta5 = -PI / 2
    xWgrip = xWgrip + 150
    yWgrip = yWgrip - 150
    zWgrip = zWgrip - 10

    x_cen = xWgrip - L[9] * math.cos(math.radians(yaw_WgripDegree))
    y_cen = yWgrip - L[9] * math.sin(math.radians(yaw_WgripDegree))
    z_cen = zWgrip

    R = math.sqrt(x_cen ** 2 + y_cen ** 2)
    beta = math.atan2(y_cen, x_cen)
    alpha = math.asin((L[2] - L[4] + L[6]) / R)
    theta1 = beta - alpha

    theta6 = theta1 + PI / 2 - math.radians(yaw_WgripDegree)

    x_3end = x_cen - L[7] * math.cos(theta1) + (L[6] + 27) * np.sin(theta1)
    y_3end = y_cen - L[7] * math.sin(theta1) - (L[6] + 27) * np.cos(theta1)
    z_3end = L[10] + L[8] + z_cen

    R_3end = math.sqrt(x_3end ** 2 + y_3end ** 2)
    h = math.sqrt(R_3end ** 2 + (z_3end - L[1]) ** 2)
    phi = math.acos((L[3] ** 2 + L[5] ** 2 - h ** 2) / (2 * L[3] * L[5]))
    theta3 = PI - phi

    gamma = math.atan2(z_3end - L[1], R_3end)
    theta2 = -(math.acos((h ** 2 + L[3] ** 2 - L[5] ** 2) / (2 * L[3] * h)) + gamma)

    theta4 = -(theta3 + theta2)

    print(np.rad2deg([theta1, theta2, theta3, theta4, theta5, theta6]))
    print(np.rad2deg(lab_fk(theta1, theta2, theta3, theta4, theta5, theta6)))

    # ==============================================================#
    return lab_fk(theta1, theta2, theta3, theta4, theta5, theta6)



