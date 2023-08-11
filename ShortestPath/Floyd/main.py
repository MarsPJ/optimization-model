import networkx as nx
import matplotlib.pyplot as plt

# 创建图并添加节点、边以及权重
G = nx.DiGraph()

# 添加节点和边
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2, {'weight': 2}),
                  (1, 3, {'weight': 4}),
                  (2, 3, {'weight': 1}),
                  (2, 4, {'weight': 7}),
                  (3, 4, {'weight': 3}),
                  (3, 5, {'weight': 5}),
                  (4, 5, {'weight': 2})])

# 使用 Floyd-Warshall 算法计算所有节点对的最短路径
shortest_paths = dict(nx.floyd_warshall(G, weight='weight'))

# 打印所有节点对的最短路径
for source in shortest_paths:
    for target in shortest_paths[source]:
        print(f"Shortest path from {source} to {target}: {shortest_paths[source][target]}")

# 绘制原始图
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_color='black')
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.show()
