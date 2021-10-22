import numpy as np
from numpy import linalg as la

x = np.arcsin(0.027)
print(x)
def lab_invk(xWgrip, yWgrip, zWgrip, yaw_WripDegree):
    L1, L2, L3, L4, L5, L6, L7, L8, L9, L10 = 0.152, 0.12, 0.244, 0.93, 0.213, 0.83, 0.83, 0.82, 0.0535, 0.059
    xcen = xWgrip - np.cos(yaw_WripDegree)*L9
    ycen = yWgrip - np.sin(yaw_WripDegree)*L9
    zcen = zWgrip + L10

    # x = np.arcsin((0.027+L6)/np.sqrt(xcen**2 + ycen**2))
    x = (0.027 + L6) / np.sqrt(xcen ** 2 + ycen ** 2)
    print(x)

    theta1 = 90*(np.pi/180) - np.arctan(ycen/xcen) - x
    theta6 = 90*(np.pi/180) - yaw_WripDegree + theta1
    theta5 = -90*(np.pi/180)

    xend = xcen - L7
    yend = xcen*np.tan(theta1)
    zend = zcen + L8 + L10

    H2 = xend**2 + (zend - L1)**2
    phi3 = np.arccos((L3**2 + L5**2 - H2)/(2*L3*L5))
    theta3 = 180*(np.pi/180) - phi3

    alpha = np.arccos((L3**2 + H2 - L5**2)/(2*L3*L5))
    beta = np.arccos(xend/np.sqrt(H2))
    theta2 = alpha + beta

    theta4 = theta3 - theta2

    return theta1, theta2, theta3, theta4, theta5, theta6

print(lab_invk(0.05,0.05,0.05,0))