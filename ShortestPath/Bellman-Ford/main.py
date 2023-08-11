import networkx as nx

# 创建有向图并添加节点、边以及权重（包括负权重）
G = nx.DiGraph()

# 添加节点和有向边（包括负权重）
G.add_edges_from([(1, 2, {'weight': 2}),
                  (1, 3, {'weight': -3}),  # 负权重
                  (2, 3, {'weight': 1}),
                  (2, 4, {'weight': -5}),  # 负权重
                  (3, 4, {'weight': 3}),
                  (3, 5, {'weight': -2}),  # 负权重
                  (4, 5, {'weight': 2})])

# 指定起始节点和终点节点
source = 1
target = 5

# 使用 Bellman-Ford 算法计算特定源点到终点的最短路径
try:
    shortest_path_length, shortest_path = nx.single_source_bellman_ford(G, source=source, target=target, weight='weight')

    print(f"Shortest path from {source} to {target}:")
    print("Length:", shortest_path_length)
    print("Path:", shortest_path)

except nx.NetworkXNoPath:
    print(f"No path from {source} to {target}.")
except nx.NetworkXUnbounded:
    print("Graph contains a negative weight cycle.")
