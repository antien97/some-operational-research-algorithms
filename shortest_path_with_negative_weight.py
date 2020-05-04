import numpy as np

infinity = float("inf")
dismat = np.array([[0,-1,-2,3,infinity,infinity,infinity,infinity],
                   [6,0,infinity,infinity,2,infinity,infinity,infinity],
                   [infinity,-3,0,-5,infinity,1,infinity,infinity],
                   [infinity,infinity,infinity,0,infinity,infinity,2,infinity],
                   [infinity,-1,infinity,infinity,0,infinity,infinity,infinity],
                   [infinity,infinity,infinity,infinity,1,0,1,7],
                   [infinity,infinity,infinity,-1,infinity,infinity,0,infinity],
                   [infinity,infinity,infinity,infinity,-3,infinity,-5,0]])

n = dismat.shape[0]
path,pathi,d,di = [],[],[],[]
for i in range(n):
    di.append(dismat[0][i])
    pathi.append(i)
d.append(di)
path.append(pathi)
while len(d) == 1 or d[-1] != d[len(d) - 2]:
    pathi,di = [],[]
    for i in range(n):
        minVal = infinity
        v = -1
        for j in range(n):
            if d[-1][j] + dismat[j][i] < minVal:
                minVal = d[-1][j] + dismat[j][i]
                v = j
        di.append(minVal)
        pathi.append(v)
    d.append(di)
    path.append(pathi)
print(d)
print(path)