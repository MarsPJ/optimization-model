from MyProblem import MyProblem
import geatpy as ea


if __name__ == '__main__':
    problem = MyProblem()
    # 构建算法
    algorithm = ea.moea_NSGA2_templet(
        problem,
        ea.Population(Encoding='BG', NIND=50),
        MAXGEN=200,  # 最大进化代数
        logTras=0)  # 表示每隔多少代记录一次日志信息，0表示不记录。
    algorithm.mutOper.Pm = 0.2  # 修改变异算子的变异概率
    algorithm.recOper.XOVR = 0.9  # 修改交叉算子的交叉概率
    # 求解
    res = ea.optimize(algorithm,
                      verbose=False,
                      drawing=1,
                      outputMsg=True,
                      drawLog=False,
                      saveFlag=False)
    print(res)