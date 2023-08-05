"""
缺陷：
1.只能求解完全图
2.蚂蚁数量和城市数量要相当，否则
Traceback (most recent call last):
  File "C:/Users/Mars/Desktop/优化类模型/AntColonyAlgorithm/main.py", line 64, in <module>
    pathtable[numcity:, 0] = np.random.permutation(range(0, numcity))[:numant - numcity]  # 然后将剩余的蚂蚁的起始城市设置为前numcity个城市中随机选择的一些城市的索引
ValueError: could not broadcast input array from shape (20) into shape (380)
3.参数不能自适应变化

"""


import random

import numpy as np
import matplotlib.pyplot as plt

coordinates = np.array([[0.8223865, 0.90249145],
                        [0.87299287, 0.97785658],
                        [0.58388132, 0.31408447],
                        [0.72751158, 0.05415505],
                        [0.60553193, 0.00697702],
                        [0.45564878, 0.15191931],
                        [0.411461, 0.17028803],
                        [0.42169505, 0.29723746],
                        [0.34342426, 0.13354594],
                        [0.26429325, 0.17590559],
                        [0.19763023, 0.12130362],
                        [0.13727432, 0.25075126],
                        [0.00319099, 0.38633692],
                        [0.24217939, 0.40168494],
                        [0.21614921, 0.42319542],
                        [0.26362807, 0.54363507],
                        [0.0312916, 0.64368314],
                        [0.36832452, 0.75778461],
                        [0.50299907, 0.50413817],
                        [0.65584064, 0.93553257]])


def getdistmat(coordinates):
    num = coordinates.shape[0]
    distmat = np.zeros((20, 20))
    for i in range(num):
        for j in range(i, num):
            distmat[i][j] = distmat[j][i] = np.linalg.norm(coordinates[i] - coordinates[j])
    return distmat


distmat = getdistmat(coordinates)  # 城市的距离矩阵
numant = 40  # 蚂蚁个数
numcity = coordinates.shape[0]  # 城市个数
alpha = 1  # 信息素重要程度因子
beta = 5  # 启发函数重要程度因子
rho = 0.1  # 信息素的挥发速度
Q = 1
iter = 0
itermax = 250
"""
distmat是城市之间的距离矩阵，np.diag([1e10] * numcity)创建了一个对角线元素为1e10、其他元素为0的方阵，将其加到distmat上，
是为了避免出现除以零的错误（因为城市与自身的距离为0）。
1e10是一个足够大的数，它的倒数接近于零，表示蚂蚁不希望（或者说，不能）选择当前城市作为下一个要访问的城市。
"""
etatable = 1.0 / (distmat + np.diag([1e10] * numcity))  # 启发函数矩阵，表示蚂蚁从城市i转移到矩阵j的期望程度
pheromonetable = np.ones((numcity, numcity))  # 信息素矩阵
pathtable = np.zeros((numant, numcity)).astype(int)  # 路径记录表，记录每个蚂蚁访问城市的顺序，第i行j列表示第i个蚂蚁访问的第j个城市的index
lengthaver = np.zeros(itermax)  # 各代路径的平均长度
lengthbest = np.zeros(itermax)  # 各代及其之前遇到的最佳路径长度
pathbest = np.zeros((itermax, numcity))  # 各代及其之前遇到的最佳路径顺序

while iter < itermax:
    # 随机产生各个蚂蚁的起点城市
    if numant <= numcity:  # 城市数比蚂蚁数多
        pathtable[:, 0] = np.random.permutation(range(0, numcity))[:numant]  # 将城市索引进行随机打乱，然后取前numant个索引作为numant个蚂蚁的起始城市
    else:  # 蚂蚁数比城市数多，需要补足
        pathtable[:numcity, 0] = np.random.permutation(range(0, numcity))[:]  # 先将城市分配给前numcity个蚂蚁
        pathtable[numcity:, 0] = np.random.permutation(range(0, numcity))[:numant - numcity]  # 然后将剩余的蚂蚁的起始城市设置为前numcity个城市中随机选择的一些城市的索引
    length = np.zeros(numant)  # 计算各个蚂蚁的路径距离
    # 第i个蚂蚁访问
    for i in range(numant):
        visiting = pathtable[i, 0]  # 当前所在的城市
        unvisited = set(range(numcity))  # 未访问的城市,以集合的形式存储{}
        unvisited.remove(visiting)  # 删除元素；利用集合的remove方法删除存储的数据内容
        # 第i个蚂蚁访问第j个城市（j只表示顺序，不代表城市序号）
        for j in range(1, numcity):  # 循环numcity-1次，访问剩余的numcity-1个城市
            # 每次用轮盘法选择下一个要访问的城市
            listunvisited = list(unvisited)
            probtrans = np.zeros(len(listunvisited))  # 转移概率值probtrans

            """计算转移概率"""
            for k in range(len(listunvisited)):
                #  \ 表示续行符
                probtrans[k] = np.power(pheromonetable[visiting][listunvisited[k]], alpha) \
                               * np.power(etatable[visiting][listunvisited[k]], beta)
            cumsumprobtrans = (probtrans / sum(probtrans)).cumsum()
            cumsumprobtrans -= np.random.rand()


            # k = listunvisited[  (  np.where(cumsumprobtrans>0)[0]  )  [0]]  # python3中原代码运行bug，类型问题；鉴于此特找到其他方法
            # by pzj 考虑cumsumprobtrans没有元素>0的情况
            indices = np.where(cumsumprobtrans > 0)[0]
            if len(indices) > 0:
                k = listunvisited[indices[0]]
            else:
                k = listunvisited[random.randint(0, len(listunvisited)-1)]  # 没有>0时，说明信息素普遍都很小，此时可以随机选择一个城市
            # 通过where（）方法寻找矩阵大于0的元素的索引并返回ndarray类型，然后接着载使用[0]提取其中的元素，用作listunvisited列表中
            # 元素的提取（也就是下一轮选的城市）

            pathtable[i, j] = k  # 添加到路径表中（也就是蚂蚁走过的路径)
            unvisited.remove(k)  # 然后在为访问城市set中remove（）删除掉该城市
            length[i] += distmat[visiting][k]
            visiting = k
        length[i] += distmat[visiting][pathtable[i, 0]]  # 蚂蚁的路径距离包括最后一个城市和第一个城市的距离
        # 包含所有蚂蚁的一个迭代结束后，统计本次迭代的若干统计参数
    lengthaver[iter] = length.mean()
    if iter == 0:
        lengthbest[iter] = length.min()  # 最短路径长度
        pathbest[iter] = pathtable[length.argmin()].copy()  # 最短路径的访问顺序  .copy深拷贝
    else:
        if length.min() > lengthbest[iter - 1]:
            lengthbest[iter] = lengthbest[iter - 1]
            pathbest[iter] = pathbest[iter - 1].copy()
        else:
            lengthbest[iter] = length.min()
            pathbest[iter] = pathtable[length.argmin()].copy()
    # 更新信息素
    # 新的信息素 = 挥发后残余的信息素 + 每条路径增加的信息素之和
    # 每条路径增加的信息素 = (Q/每个蚂蚁总共走的路径长度)的和
    changepheromonetable = np.zeros((numcity, numcity))  # 每条路径增加的信息素之和
    for i in range(numant):
        for j in range(numcity - 1):
            changepheromonetable[pathtable[i, j]][pathtable[i, j + 1]] += Q / distmat[pathtable[i, j]][
                pathtable[i, j + 1]]  # 计算信息素增量
        changepheromonetable[pathtable[i, j + 1]][pathtable[i, 0]] += Q / distmat[pathtable[i, j + 1]][pathtable[i, 0]]  # 加上回环的信息素增量
    pheromonetable = (1 - rho) * pheromonetable + changepheromonetable  # 计算信息素公式
    iter += 1  # 迭代次数指示器+1
    print("iter:", iter)

# 做出平均路径长度和最优路径长度
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
axes[0].plot(lengthaver, 'k', marker=u'')
axes[0].set_title('Average Length')
axes[0].set_xlabel(u'iteration')

axes[1].plot(lengthbest, 'k', marker=u'')
axes[1].set_title('Best Length')
axes[1].set_xlabel(u'iteration')
fig.savefig('average_best.png', dpi=500, bbox_inches='tight')
plt.show()
print(lengthbest[-1])

# 作出找到的最优路径图
bestpath = pathbest[-1]
plt.plot(coordinates[:, 0], coordinates[:, 1], 'r.', marker=u'$\cdot$')
plt.xlim([0, 1])
plt.ylim([0, 1])

for i in range(numcity - 1):
    m = int(bestpath[i])
    n = int(bestpath[i + 1])
    plt.plot([coordinates[m][0], coordinates[n][0]], [coordinates[m][1], coordinates[n][1]], 'k')
plt.plot([coordinates[int(bestpath[0])][0], coordinates[int(n)][0]],
         [coordinates[int(bestpath[0])][1], coordinates[int(n)][1]], 'b')
ax = plt.gca()
ax.set_title("Best Path, length is % s" % lengthbest[-1])
ax.set_xlabel('X axis')
ax.set_ylabel('Y_axis')

plt.savefig('best path.png', dpi=500, bbox_inches='tight')
plt.show()