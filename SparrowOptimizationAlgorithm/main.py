import random
import numpy as np
import SSA as SSA
import matplotlib
from matplotlib import pyplot as plt

# 解决plt中文乱码
font = {
    'family':'SimHei',
    'weight':'bold',
    'size':12
}
matplotlib.rc("font", **font)


def fun1(X):
    result = np.sum(X ** 4)
    return result


'''主函数 '''
# #设置参数
pop = 30 #种群数量
MaxIter = 500 #最大迭代次数
dim = 30#维度
lb = np.min(-100)*np.ones([dim, 1]) #下边界
ub = np.max(100)*np.ones([dim, 1])#上边界
#适应度函数选择
fobj = fun1

GbestScore, GbestPositon, Curve, Space = SSA.Tent_SSA(pop, dim, lb, ub, MaxIter, fobj)
print('SSA最优适应度值：',GbestScore)
print('SSA最优位置：',GbestPositon)
# print(Curve)
plt.plot(range(1, MaxIter + 1), Curve)
plt.title("迭代次数-最优值")
plt.xlabel("迭代次数")
plt.ylabel("最优值")
plt.show()
