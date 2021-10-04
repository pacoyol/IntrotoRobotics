import numpy as np
import math
import scipy as scp
from scipy import linalg as la

theta = np.array([[0.15, -0.29, 0.34, -0.11, 0.72]])
S1= [0,0,0,0,0,1]
S2= [0,0,0,0,0,1]
S3= [1,0,0,0,4,0]
S4= [0,1,0,-6,0,0]
S5= [0,1,0,-6,0,-2]
def Conversion(S):
    # S here is array of the screw axis
    w_1 = S[0]
    w_2 = S[1]
    w_3 = S[2]
    v_1 = S[3]
    v_2 = S[4]
    v_3 = S[5]

    S_bracket = np.array([[0, -w_3, w_2, v_1],[w_3, 0, -w_1, v_2],[-w_3, w_1, 0, v_3], [0,0,0,0]])
    return S_bracket
p1= Conversion(S1)
p2= Conversion(S2)
p3= Conversion(S3)
p4= Conversion(S4)
p5= Conversion(S5)
M= [[0,1,0,2],[0,0,1,-6],[1,0,0,0],[0,0,0,1]]

a=la.expm(p1*theta[0][0])@la.expm(p2*theta[0][1])@ la.expm(p3*theta[0][2])@la.expm(p4*theta[0][3])@la.expm(p5*theta[0][4])@M
print(a)

A = [[ 0.61 , 1  , 0 , -2.02] , [-0.33348709, 0,  0.94275467, -3.84235821] , [ 0.94275467, 0 , 0.33348709 ,-3.26950793] , [ 0 , 0  , 0  , 1 ]]
print(A)