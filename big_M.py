import numpy as np

#单纯形法--大M法
# min Z = -3X1 + X2 + x3
# X1 - 2X2 + x3 <= 11
# -4X1 + X2 + 2x3 >= 3
# -2X1 + x3 = 1
# X1 , X2, x3 >= 0

def getVarNum(b):        #得到松弛变量、剩余变量、人工变量的总个数
    number = 0
    for bi in b:
        if bi[-2] == '<=':
            number += 1
        if bi[-2] == '>=':
            number += 2
        if bi[-2] == '=':
            number += 1
    return number

def getSimTable(z,b,M,varNumber):    #得到初始单纯形表的所有信息
    lengthZ = len(z)
    a = []
    cb = []
    xb = []

    for i in range(len(b)):
        if b[i][-2] == '<=':
            lengthZ += 1
            z += [0]
            ai = [0 for j in range(varNumber)]
            if i != 0:
                for aa in a:
                    if -1 in aa:
                        ai[i] = 0
                        ai[i + 1] = 1
                        break
                    else:
                        ai[i] = 1
            else:
                ai[i] = 1
            a.append(ai)
            cb.append(0)
            xb.append(lengthZ)
        elif b[i][-2] == '>=':
            lengthZ += 2
            z += [0, M]
            ai = [0 for j in range(varNumber)]
            ai[i] = -1
            ai[i + 1] = 1
            a.append(ai)
            cb.append(M)
            xb.append(lengthZ)
        elif b[i][-2] == '=':
            lengthZ += 1
            z += [M]
            ai = [0 for j in range(varNumber)]
            if i != 0:
                for aa in a:
                    if -1 in aa:
                        ai[i] = 0
                        ai[i + 1] = 1
                        break
                    else:
                        ai[i] = 1
            else:
                ai[i] = 1
            a.append(ai)
            cb.append(M)
            xb.append(lengthZ)

    m = np.zeros(( len(b), lengthZ + 1))
    c = z + [0]
    for i in range(len(b)):
        m[i] = b[i][:-2] + a[i] + [b[i][-1]]
    return m,cb,c,xb

M = 100000                     #大M，一个足够大的正数
z = [-3,1,1]
b = [[1,-2,1,'<=',11],[-4,1,2,'>=',3],[-2,0,1,'=',1]]

varNum = getVarNum(b)
m,cb,c,xb = getSimTable(z,b,M,varNum)    #初始单纯形表信息
cMinusZ = []

judge = False
while not judge:
    for i in range(m.shape[1] - 1):
        cz = 0
        for j in range(m.shape[0]):
            cz += m[j][i] * cb[j]
        cMinusZ.append(c[i] - cz)
    if min(cMinusZ) >= 0:
        judge = True
        break
    else:
        Xin = cMinusZ.index(min(cMinusZ))            #换入变量，目标函数为求最小值，因此这里用min方法
        minVal = float("inf")
        infinite = True
        for i in range(m.shape[0]):
            if m[i][Xin] != 0:
                if m[i][-1] / m[i][Xin] < minVal and m[i][-1] / m[i][Xin] > 0:
                    minVal = m[i][-1]/m[i][Xin]
                    Xout = i                      #换出变量
                    infinite = False
        if infinite is True:
            print("问题无界")
            exit()
        m[Xout] = m[Xout] / m[Xout][Xin]
        for i in range(m.shape[0]):
            if i != Xout and m[i][Xin] != 0:
                m[i] -= m[Xout] * m[i][Xin]
        cb[Xout] = c[Xin]
        xb[Xout] = Xin + 1
    cMinusZ = []
solution = [0 for i in range(m.shape[1] - 1)]
for i in range(len(xb)):
    solution[xb[i] - 1] = m[i][-1]

print("最优解：" + str(solution))
print("目标函数最小值：" + str(-3 * solution[0] + solution[1] + solution [2]))