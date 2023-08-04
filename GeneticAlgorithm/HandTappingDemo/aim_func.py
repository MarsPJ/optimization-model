# -*- coding: utf-8 -*-
"""
aimfunc.py - 目标函数文件
描述:
    目标：max f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2)
    约束条件：
        x1 != 10
        x2 != 5
        x1 ∈ [-3, 12.1] # 变量范围是写在遗传算法的参数设置里面
        x2 ∈ [4.1, 5.8]
"""
import numpy as np


def aim_func(Phen, CV):
    # Phen ：表现型矩阵
    x1 = Phen[:,[0]]
    x2 = Phen[:,[1]]
    f = 21.5 + x1 * np.sin(4 * np.pi * x1) + x2 * np.sin(20 * np.pi * x2);
    exIdx1 = np.where(x1 == 10)
    exIdx2 = np.where(x2 == 5)
    CV[exIdx1] = 1
    CV[exIdx2] = 1
    return [f, CV]



