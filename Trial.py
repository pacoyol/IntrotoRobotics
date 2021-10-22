import numpy as np

Slist = np.array([[    0,    0,    1,    0,   -1,    0],
                  [    0,    1,    0,    0,    0,    1],
                  [    0,    1,    0,    1,    0, 2.73],
                  [    0,    1,    0,-0.73,    0, 3.73],
                  [    0,    0,    0,    0,    0,    1],
                  [    0,    0,    1,    0,    -3.73,0]])

for i in reversed(range(len(Slist))):
    print(Slist[i])
    print(Slist[i][2])