import numpy as np
import modern_robotics as mr

T_sa = np.array([[0,-1, 0, 0],
                 [0, 0,-1, 0],
                 [1, 0, 0, 1],
                 [0, 0, 0, 1]])
print("\nQuestion 1:\n", np.array2string(T_sa, separator=',')) # question 1

T_sb = np.array([[1, 0, 0, 0],
                 [0, 0, 1, 2],
                 [0,-1, 0, 0],
                 [0, 0, 0, 1]])

T_bs = mr.TransInv(T_sb)
print("\nQuestion 2:\n", np.array2string(T_bs, separator=',')) # question 2

T_as = mr.TransInv(T_sa)
T_ab = np.dot(T_as, T_sb)
print("\nQuestion 3:\n", np.array2string(T_ab, separator=',')) # question 3

p_b = np.array([1, 2, 3])
p_b_homo = np.append(p_b, 1)
p_s_homo = np.dot(T_sb, p_b_homo)
p_s = np.delete(p_s_homo, 3)
print("\nQuestion 5:\n", np.array2string(p_s, separator=',')) # question 5

V_s = np.array([3, 2, 1, -1, -2, -3])
Ad_T_as = mr.Adjoint(T_as)
V_a = np.dot(Ad_T_as, V_s)
print("\nQuestion 7:\n", np.array2string(V_a, separator=',')) # question 7

MatrixLog_T_sa = mr.MatrixLog6(T_sa)
MatrixLog_T_sa_vec = mr.se3ToVec(MatrixLog_T_sa)
theta_MatrixLog_T_sa = mr.AxisAng6(MatrixLog_T_sa_vec)[1]
print("\nQuestion 8:\n", round(theta_MatrixLog_T_sa, 2)) # question 8

exp_coord_q9_vec = np.array([0, 1, 2, 3, 0, 0])
exp_coord_q9_se3 = mr.VecTose3(exp_coord_q9_vec)
MatrixExp_exp_coord_q9 = mr.MatrixExp6(exp_coord_q9_se3)
MatrixExp_exp_coord_q9_off = np.around(MatrixExp_exp_coord_q9, decimals=2)
print("\nQuestion 9:\n", np.array2string(MatrixExp_exp_coord_q9_off, separator=',', suppress_small=True)) # question 9

F_b = np.array([1, 0, 0, 2, 1, 0])
Ad_T_bs = mr.Adjoint(T_bs)
Ad_T_bs_trans = np.transpose(Ad_T_bs)
F_s = np.dot(Ad_T_bs_trans, F_b)
print("\nQuestion 10:\n", np.array2string(F_s, separator=',')) # question 10

T_q11 = np.array([[ 0, -1,  0,  3],
                  [ 1,  0,  0,  0],
                  [ 0,  0,  1,  1],
                  [ 0,  0,  0,  1]])
T_q11_inv = mr.TransInv(T_q11)
print("\nQuestion 11:\n", np.array2string(T_q11_inv, separator=',')) # question 11

V_q12 = np.array([1, 0, 0, 0, 2, 3])
V_q12_se3 = mr.VecTose3(V_q12)
print("\nQuestion 12:\n", np.array2string(V_q12_se3, separator=',')) # question 12

vec_s_q13 = np.array([1, 0, 0])
point_p_q13 = np.array([0, 0, 2])
h_q13 = 1
S_q13 = mr.ScrewToAxis(point_p_q13, vec_s_q13, h_q13)
print("\nQuestion 13:\n", np.array2string(S_q13, separator=',')) # question 13

MatrixExp_q14 = np.array([[     0, -1.5708, 0,  2.3562],
                          [1.5708,       0, 0, -2.3562],
                          [     0,       0, 0,       1],
                          [     0,       0, 0,       0]])
T_q14 = mr.MatrixExp6(MatrixExp_q14)
T_q14_off = np.around(T_q14, decimals=0)
print("\nQuestion 14:\n", np.array2string(T_q14_off, separator=',', suppress_small=True)) # question 14

T_q15 = np.array([[ 0, -1, 0, 3],
                  [ 1,  0, 0, 0],
                  [ 0,  0, 1, 1],
                  [ 0,  0, 0, 1]])
MatrixLog_T_q15 = mr.MatrixLog6(T_q15)
MatrixLog_T_q15_off = np.around(MatrixLog_T_q15, decimals=2)
print("\nQuestion 15:\n", np.array2string(MatrixLog_T_q15_off, separator=',', suppress_small=True)) # question 15