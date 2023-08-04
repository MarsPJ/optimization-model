import numpy as np
import geatpy as ea
from aim_func import aim_func
import time

"""=====================================变量设置==============================="""
x1 = [-3, 12.1]  # 第一个决策变量范围
x2 = [4.1, 5.7]  # 第二个决策变量范围
b1 = [1, 1]  # 第一个决策变量边界，第一列表示左边界，第二列表示右边界，1表示包含边界，0表示不包含
b2 = [1, 1]  # 第二个决策变量边界
ranges = np.vstack([x1, x2]).T  # 自变量范围矩阵，vstack表示垂直拼凑，.T表示转置，使得结果的第一行为所有决策变量的上界，第二行为下界
borders = np.vstack([b1, b2]).T  # 自变量的边界矩阵，结果的第一行为所有决策变量的上界是否包含边界，第二行表示下界是否包含边界
varTypes = np.array([0, 0])  # 决策变量的类型，0表示连续变量，1表示离散变量
"""===================================染色体编码设置=============================="""
Encoding = 'BG'  # BG表示采用二进制/格雷码进行编码
codes = [0, 0] # 决策变量的编码方式，0为二进制编码，1为格雷编码
precisions = [4, 4]  # 二进制编码串解码后能表示的决策变量的精度可达到的小数点位数
scales = [0, 0]  # 0表示采用算术刻度，1表示采用对数刻度，从2.5.0版本开始，取消了对对数刻度的支持
FieldD = ea.crtfld(Encoding, varTypes, ranges, borders, precisions, codes, scales);  # 译码矩阵生成函数，返回二进制/格雷码种群译码矩阵
"""================================遗传算法参数设置================================"""
NIND = 100  # 种群个体数目
MAXGEN = 200   # 最大遗传代数
max_or_min = [-1]  # 1表示目标函数需要最小化，-1表示最大化
max_or_min = np.array(max_or_min)  # 转化为numpy array 行向量
# print(max_or_min.shape) // (1,)
select_style = 'rws'  # 选择（抽样）方式：采用轮盘赌选择
rec_style = 'xovdp'  # 交叉（重组）方式：采用两点交叉
mut_style = 'mutbin'  # 变异方式：二进制变异算子(Mutation for binary chromosomes)(均匀变异)
Lind = int(np.sum(FieldD[0, :]))  # 计算染色体长度，[lens;           每个决策变量编码后在染色体中所占的长度。...]，
pc = 0.1  # 交叉概率
pm = 1/Lind  # 变异概率，与染色体长度成反比
obj_trace = np.zeros((MAXGEN, 2))  # 定义目标函数值记录器，第i行1列表示第i+1代种群的目标函数值均值，第2列表示第i+1代最优个体的目标函数值
var_trace = np.zeros((MAXGEN, Lind))  # 染色体记录器，记录历代最优个体的染色体
"""=================================开始遗传算法====================================="""
start_time = time.time()  # 计时开始
Chrom = ea.crtpc(Encoding, NIND, FieldD)  # 生成种群染色体矩阵, crtpc : Create Population's Chromosomes创建一个种群染色体矩阵
variable = ea.bs2ri(Chrom, FieldD)  # 对初始种群解码，Binary strings to reals & integers
CV = np.zeros((NIND, 1))  # 初始化一个CV矩阵，由于未确定初始个体是否满足约束条件，CV矩阵元素初始化全为0，即暂时认为所有个体都是可行解个体
ObjV, CV = aim_func(variable, CV)  # 计算初始种群个体的目标函数值和CV矩阵
FitnV = ea.ranking(ObjV, CV, max_or_min) # 根据目标函数大小分配适应度值，默认目标函数值越高，适应度越低，因此需要传入max_or_min改变
best_ind = np.argmax(FitnV) # 计算当代最优个体的序号
# 开始进化
for gen in range(MAXGEN):
    SelChrom = Chrom[ea.selecting(select_style, FitnV, NIND - 1), :]  # 选择（抽样），只选择NIND-1个个体，因为后面要加上一个best_ind
    SelChrom = ea.recombin(rec_style, SelChrom, pc)  # 交叉（重组）
    SelChrom = ea.mutate(mut_style, Encoding, SelChrom, pm)  # 变异
    # 把父代精英个体与子代的染色体进行合并，得到新的种群
    Chrom = np.vstack([Chrom[best_ind, :], SelChrom])
    Phen = ea.bs2ri(Chrom, FieldD)  # 对种群进行解码(二进制转十进制)
    ObjV, CV = aim_func(Phen, CV)  # 求种群个体的目标函数值和CV矩阵
    FitnV = ea.ranking(ObjV, CV, max_or_min)  # 根据目标函数大小分配适应度值
    # 记录
    best_ind = np.argmax(FitnV)  # 计算当代最优个体的序号
    obj_trace[gen, 0]=np.sum(ObjV)/ObjV.shape[0]  # 记录当代种群的目标函数均值
    obj_trace[gen, 1]=ObjV[best_ind]  # 记录当代种群最优个体目标函数值
    var_trace[gen, :]=Chrom[best_ind,:]  # 记录当代种群最优个体的染色体
"""===================================进化完成========================================"""
end_time = time.time() # 计时结束
ea.trcplot(obj_trace, [['种群个体平均目标函数值', '种群最优个体目标函数值']])  # 绘制图像
"""==================================输出结果========================================="""
best_gen = np.argmax(obj_trace[:, 1])
print('最优解的目标函数值：', obj_trace[best_gen, 1])
variable = ea.bs2ri(var_trace[[best_gen], :], FieldD)  # 解码得到表现型（即对应的决策变量值）,不能写成var_trace[best_gen, :], FieldD)，奇怪的bug
print("最优解的决策变量值为：")
for i in range(variable.shape[1]):
    print('x' + str(i) + '=', variable[0, i])
print('用时：', end_time - start_time, '秒')






