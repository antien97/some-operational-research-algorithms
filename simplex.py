import numpy as np
import time

#单纯形法
# max Z = 2X1 + 3X2
# X1 + 2X2 <= 8
# 4X1 + 0X2 <= 16
# 0X1 + 4X2 <= 12
# X1 , X2 > 0

z = [2,3]
b = [[1,2,8],[4,0,16],[0,4,12]]
length = len(z)
z += [0 for i in range(len(b))]
m = np.zeros((1 + len(b),length + len(b) + 1))
m[0] = z + [0]
for i in range(len(b)):
    a = [0 for j in range(len(b))]
    a[i] = 1
    m[i+1] = b[i][:-1] + a + [b[i][-1]]
judge = False
infinite = True
while not judge:
    judgeList = m[0].tolist()
    if max(judgeList) <= 0:
        judge = True
        break
    else:
        Xin = judgeList.index(max(judgeList))           #换入变量
        min = float("inf")
        for i in range(m.shape[0] - 1):
            if m[i + 1][Xin] > 0:
                infinite = False
                if m[i + 1][-1] / m[i + 1][Xin] < min and m[i + 1][-1] / m[i + 1][Xin] > 0:
                    min = m[i + 1][-1]/m[i + 1][Xin]
                    Xout = i + 1                       #换出变量
        if infinite is True:
            print("问题无界")
            exit()
        m[Xout] = m[Xout] / m[Xout][Xin]
        for i in range(m.shape[0]):
            if i != Xout and m[i][Xin] != 0:
                m[i] -= m[Xout] * m[i][Xin]
solution = [0 for i in range(m.shape[1] - 1)]
for i in range(m.shape[1] - 1):
    if m[0][i] == 0:
        for j in range(m.shape[0] - 1):
            if m[j + 1][i] == 1:
                solution[i] = m[j + 1][-1]
    else:
        solution[i] = 0
print("最优解：" + str(solution))
print("目标函数最大值：" + str(-m[0][-1]))
