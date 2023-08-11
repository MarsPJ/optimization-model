# -*- coding: utf-8 -*-
"""
MyProblem.py
描述:
    目标：max f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
    约束条件：
        x1 != 10
        x2 != 5
        x1 ∈ [-3, 12.1] # 变量范围是写在遗传算法的参数设置里面
        x2 ∈ [4.1, 5.8]
"""
import numpy as np
import geatpy as ea


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):
        name = 'MyProblem'  # 函数名称，可以随意设置
        M = 1  # 目标维数
        max_or_min = [-1] # 最大化为-1，最小化为1
        Dim = 2  # 决策变量维数
        varTypes = [0] * Dim  # 决策变量类型，0为连续（实数），1为离散（整数）
        lb = [-3, 4.1]  # 决策变量下界
        ub = [12.1, 5.8]  # 上界
        lbin = [1] * Dim  # 决策变量是否包括下边界，1表示包括，0表示不包括
        ubin = [1] * Dim  # 决策变量是否包括上边界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, max_or_min, Dim, varTypes, lb, ub, lbin, ubin)

    def aimFunc(self, pop):  # 目标函数
        x1 = pop.Phen[:, [0]]  # 获取表现型矩阵的第一列，得到所有个体的x1的值
        x2 = pop.Phen[:, [1]]  # 得到x2的值
        f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
        exIdx1 = np.where(x1 == 10)[0]
        exIdx2 = np.where(x2 == 5)[0]
        pop.CV = np.zeros((pop.sizes, 2))  # 构造CV矩阵，2列是因为有两个约束条件
        pop.CV[exIdx1, 0] = 1  # 将CV矩阵对应的第一个约束条件的位置的CV值置为不满足（置为1）
        pop.CV[exIdx2, 1] = 1  # 将CV矩阵对应的第二个约束条件的位置的CV值置为不满足（置为1）
        pop.ObjV = f  # 计算目标函数值，赋值给pop种群对象的ObjV属性

