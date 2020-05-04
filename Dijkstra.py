import numpy as np

dismat = np.array([[0,6,3,1,0,0,0,0,0],
                   [0,0,0,0,1,0,0,0,0],
                   [0,2,0,2,0,0,0,0,0],
                   [0,0,0,0,0,10,0,0,0],
                   [0,0,0,6,0,4,3,6,0],
                   [0,0,0,0,10,0,2,0,0],
                   [0,0,0,0,0,0,0,4,0],
                   [0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,2,0,0,3,0]])

p = [-1 for i in range(dismat.shape[0])]     #起始点到各点的最短距离
PT = ['T' for i in range(dismat.shape[0])]   #各点的标号
λ = [-1 for i in range(dismat.shape[0])]     #最短路中各点至前一个点的最短路
T = [float("inf") for i in range(dismat.shape[0])]    #各点的T标号值
s = []                                       #具P标号的点的集合
p[0] = 0                                     # 0为第一个获得P标号的点
PT[0] = 'P'
λ[0] = 0
T[0] = 0
s.append(0)
while len(s) != 9:
    for k in s:
        for i in range(len(dismat[k])):
            if dismat[k][i] != 0 and i not in s:
                if T[i] > p[k] + dismat[k][i]:
                    T[i] = p[k] + dismat[k][i]
                    λ[i] = k
    minVal = float("inf")
    for i in range(len(T)):
        if PT[i] != 'P' and T[i] < minVal:
            minVal = T[i]
    PT[T.index(minVal)] = 'P'
    p[T.index(minVal)] = minVal
    s.append(T.index(minVal))
print(p)
print(λ)
