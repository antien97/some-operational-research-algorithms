#指派问题
import numpy as np
from collections import Counter

def getSimMat(effMat):            #简化效率矩阵
    for i in range(effMat.shape[0]):
        if 0 in effMat[i]:
            continue
        else:
            matList = effMat[i].tolist()
            effMat[i] -= min(matList)

    for i in range(effMat.shape[1]):
        minVal = float("inf")
        for j in range(effMat.shape[0]):
            if effMat[j][i] < minVal:
                minVal = effMat[j][i]
                if minVal == 0:
                    break
        for k in range(effMat.shape[0]):
            effMat[k][i] -= minVal

def circle(effMat):             #画圈
    while 0 in effMat:
        judge = False
        for i in range(effMat.shape[0]):
            zeroCount, zeroColumn = 0, -1
            for j in range(effMat.shape[1]):
                if effMat[i][j] == 0:
                    zeroCount += 1
                    zeroColumn = j
            if zeroCount == 1:
                effMat[i][zeroColumn] = -1
                for k in range(effMat.shape[0]):
                    if k != i:
                        if effMat[k][zeroColumn] == 0:
                            effMat[k][zeroColumn] = -1000
                judge = True
            else:
                continue

        for i in range(effMat.shape[1]):
            zeroCount, zeroRow = 0, -1
            for j in range(effMat.shape[0]):
                if effMat[j][i] == 0:
                    zeroCount += 1
                    zeroRow = j
            if zeroCount == 1:
                effMat[zeroRow][i] = -1
                for k in range(len(effMat[zeroRow])):
                    if k != i:
                        if effMat[zeroRow][k] == 0:
                            effMat[zeroRow][k] = -1000
                judge = True
            else:
                continue

        if judge is False:
            maxCount = float("inf")
            leastZeroRow = -1
            leastZeroColumn = -1
            zeroColumnList = []
            for i in range(effMat.shape[0]):
                count = Counter(effMat[i])
                zeroCount = count[0]
                if zeroCount < maxCount:
                    maxCount = zeroCount
                    leastZeroRow = i
            for i in range(effMat.shape[1]):
                if effMat[leastZeroRow][i] == 0:
                    zeroColumnList.append(i)
            zeroCount = 0
            maxCount = float("inf")
            for j in zeroColumnList:
                for i in range(effMat.shape[0]):
                    if effMat[i][j] == 0:
                        zeroCount += 1
                if zeroCount < maxCount:
                    maxCount = zeroCount
                    leastZeroColumn = j
            effMat[leastZeroRow][leastZeroColumn] = -1
            for i in range(effMat.shape[1]):
                if effMat[leastZeroRow][i] == 0:
                    effMat[leastZeroRow][i] = -1000
            for i in range(effMat.shape[0]):
                if effMat[i][leastZeroColumn] == 0:
                    effMat[i][leastZeroColumn] = -1000

if __name__ == '__main__':
    efficiencyMat = np.array([[2,15,13,4],[10,4,14,15],[9,14,16,13],[7,8,11,9]])
    getSimMat(efficiencyMat)
    circle(efficiencyMat)
    efficiencyMat[efficiencyMat != -1] = 0
    efficiencyMat[efficiencyMat == -1] = 1
    print(efficiencyMat)

