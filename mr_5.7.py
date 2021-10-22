import numpy as np
from scipy.linalg import expm
import modern_robotics as mr
from numpy import linalg as la
thetalist = np.array([np.pi/2.0, np.pi/2, 1])
M_s = np.array([[-1, 0, 0, 0],
                  [0, 0, 1, 3],
                  [0, 1, 0, 2],
                  [0, 0, 0, 1]])
Slist = np.array([[0, 0,  1,  0, 0,    0],
                  [1, 0,  0,  0, 2,    0],
                  [0, 0,  0,  0, 1,    0]]).T
T_s = mr.FKinSpace(M_s, Slist, thetalist)
print("T_s",T_s.round(2))
T_bs = la.pinv(T_s)
print("Tbs",T_bs.round(2))

M_b = np.array([[-1, 0, 0, 0],
              [0, 0, 1, -2],
              [0, 1, 0, -3],
              [0, 0, 0, 1]])

Blist = np.array([[0,1,0,3,0,0],
                  [-1,0,0,0,3,0],
                  [0,0,0,0,0,1]]).T

T_b = mr.FKinBody(M_b, Blist, thetalist)
J_s = mr.JacobianSpace(Slist, thetalist)
AdTs = mr.Adjoint(T_s)
print("T_b",T_b.round(2))
J_s = mr.JacobianSpace(Slist, thetalist)
J_b = mr.JacobianBody(Blist,thetalist)
print("Correct",J_b.round(2))
Ad_bs = la.pinv(J_s)@J_b
# print(Ad_bs.round(2))
Jbb = mr.Adjoint(T_s)@J_s
print(Jbb.round(2))