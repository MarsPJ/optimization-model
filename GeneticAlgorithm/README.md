# 遗传算法

**需要的参数**

- 种群数量 NIND

- 迭代次数 MAXGEN

- 染色体是否需要采用二进制/格雷编码 Encoding

  - ‘BG’表示要进行二进制/格雷编码
  - ‘RI’表示采用实值计算即可

- 约束条件（CV）

  - **种群个体违反约束程度矩阵**(CV)：它每一行对应一个个体，每一列对应一种约束条件（可以是等式约束或不等式约束）。CV矩阵中元素小于或等于0表示对应个体满足对应的约束条件，大于0则表示不满足，且越大表示违反约束条件的程度越高。

    - 比如有两个约束条件：

    ![](C:\Users\Mars\Desktop\优化类模型\GeneticAlgorithm\img\1.png)

    - 转成CV

      ![](C:\Users\Mars\Desktop\优化类模型\GeneticAlgorithm\img\2.png)

    - 对于不等式可以这样处理

      ![](C:\Users\Mars\Desktop\优化类模型\GeneticAlgorithm\img\3.png)

- 决策变量

  - 类型 varType
  - 取值范围 lb,ub,lbin,ubin
  - 个数 Dim

- 目标函数

  - 单目标还是多目标 影响使用的算法
    - 单目标是algorithm = ea.soea_EGA_templet()
  - 目标函数个数 M
  - 最大化还是最小化 max_or_min

**TODO:**

- 还没研究多目标规划的情况