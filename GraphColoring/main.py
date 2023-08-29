import cvxpy as cp
import numpy as np

# 创建一个邻接矩阵表示图的连接关系
adjacency_matrix = np.array([
    [0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0]
])

# 图中的顶点数量
num_nodes = adjacency_matrix.shape[0]

# 最大可用颜色数
num_colors = 3

# 创建变量，表示每个顶点的颜色
colors = cp.Variable(num_nodes, integer=True)

# 约束：相邻顶点颜色不同
constraints = [colors[i] != colors[j] for i in range(num_nodes) for j in range(num_nodes) if adjacency_matrix[i][j] == 1]

# 目标函数：最小化使用的颜色数
objective = cp.Minimize(cp.max(colors) + 1)

# 创建问题并求解
problem = cp.Problem(objective, constraints)
problem.solve()

# 获取最优解
optimal_colors = colors.value

print("节点的最优着色：", optimal_colors)
