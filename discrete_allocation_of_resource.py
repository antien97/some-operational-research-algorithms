import numpy as np
#动态规划
#资源离散分配问题
#某工业部门根据国家计划的安排，拟将某种高效率的设备五台，
#分配给所属的甲、乙、丙三个工厂，各工厂若获得这种设备之后，可以为国家提供的盈利如下表所示。
#问：这五台设备如何分配给各工厂，才能使国家得到的盈利最大。

mat = np.array([[0,0,0,],
                [3,5,4],
                [7,10,6],
                [9,11,11],
                [12,11,12],
                [13,11,12]])
mat_new = mat.copy()
m = mat.shape[0]
n = mat.shape[1]
bestChoice = np.zeros((m,n)).astype(int)
for k in range(n-1):
    for i in range(m):
        max = 0
        for j in range(i+1):
            if mat[j][n-2-k] + mat_new[i-j][n-1-k] > max:
                max = mat[j][n-2-k] + mat_new[i-j][n-1-k]
                bestChoice[i][n-2-k] = j
                bestChoice[i][n-1-k] = i-j
        mat_new[i][n-2-k] = max              #根据算出来的每一阶段的最优价格不断更新价格表与最佳选择表
print("最大盈利为：")
print(mat_new[m-1][0])
print("最佳分配方案为：")
print(bestChoice[m-1][0])
for i in range(n-2):
    print(bestChoice[m-1][i+1] - bestChoice[m-1][i+2])
print(bestChoice[-1][-1])
# total_max = 0
# a =0
# for i in range(m):
#     if mat[i][0] + mat[bestChoice[m-i-1][n-2]][n-2] + mat[bestChoice[m-i-1][n-1]][n-1] > total_max:
#         total_max = mat[i][0] + mat[bestChoice[m-i-1][n-2]][n-2] + mat[bestChoice[m-i-1][n-1]][n-1]
#         a = i
# print(a,bestChoice[m-a-1][n-2],bestChoice[m-a-1][n-1])
# print(total_max)