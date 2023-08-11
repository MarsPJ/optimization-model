import numpy as np
import geatpy as ea
from GAFrame.SingleObjectOptimization.MyProblem import MyProblem

# =================实例化问题对象====================
problem = MyProblem()
# ==================构建算法=========================
Encoding = 'BG'
NIND = 100  # 种群个体数量
MAXGEN = 200  # 最大迭代次数
logTras = 1  # 每隔多少代记录一次日志信息
algorithm = ea.soea_EGA_templet(problem, ea.Population(Encoding=Encoding, NIND=NIND), MAXGEN=MAXGEN, logTras=logTras)
# =====================求解==========================
# algorithm.mutOper.Pm = 0.2 # 修改变异算子的变异概率
# algorithm.recOper.XOVR = 0.9 # 修改交叉算子的交叉概率
res = ea.optimize(algorithm, verbose=True, drawing=1, outputMsg=True, drawLog=False)
"""
    输入参数:
        algorithm : <class: class> - 算法类的引用。
        seed      : int  - 随机数种子。
        prophet   : <class: Population> / Numpy ndarray - 先验知识。可以是种群对象，
                                                          也可以是一组或多组决策变量组成的矩阵（矩阵的每一行对应一组决策变量）。
        verbose   : bool - 控制是否在输入输出流中打印输出日志信息。
                           该参数将被传递给algorithm.verbose。
                           如果algorithm已设置了该参数的值，则调用optimize函数时，可以不传入该参数。
        drawing   : int  - 算法类控制绘图方式的参数，
                           0表示不绘图；
                           1表示绘制最终结果图；
                           2表示实时绘制目标空间动态图；
                           3表示实时绘制决策空间动态图。
                           该参数将被传递给algorithm.drawing。
                           如果algorithm已设置了该参数的值，则调用optimize函数时，可以不传入该参数。
        outputMsg : bool - 控制是否输出结果以及相关指标信息。
        drawLog   : bool - 用于控制是否根据日志绘制迭代变化图像。
        saveFlag  : bool - 控制是否保存结果。
        dirName   : str  - 文件保存的路径。当缺省或为None时，默认保存在当前工作目录的'result of job xxxx-xx-xx xxh-xxm-xxs'文件夹下。
    输出参数:
        result    : dict - 一个保存着结果的字典。内容为：
                           {'success': True or False,  # 表示算法是否成功求解。
                            'stopMsg': xxx,  # 存储着算法停止原因的字符串。
                            'optPop': xxx,  # 存储着算法求解结果的种群对象。如果无可行解，则optPop.sizes=0。optPop.Phen为决策变量矩阵，optPop.ObjV为目标函数值矩阵。
                            'lastPop': xxx,  # 算法进化结束后的最后一代种群对象。
                            'Vars': xxx,  # 等于optPop.Phen，此处即最优解。若无可行解，则Vars=None。
                            'ObjV': xxx,  # 等于optPop.ObjV，此处即最优解对应的目标函数值。若无可行解，ObjV=None。
                            'CV': xxx,  # 等于optPop.CV，此处即最优解对应的违反约束程度矩阵。若无可行解，CV=None。
                            'startTime': xxx,  # 程序执行开始时间。
                            'endTime': xxx,  # 程序执行结束时间。
                            'executeTime': xxx,  # 算法所用时间。
                            'nfev': xxx,  # 算法评价次数
                            'gd': xxx,  # (多目标优化且给定了理论最优解时才有) GD指标值。
                            'igd': xxx,  # (多目标优化且给定了理论最优解时才有) IGD指标值。
                            'hv': xxx,  # (多目标优化才有) HV指标值。
                            'spacing': xxx}  # (多目标优化才有) Spacing指标值。

"""


