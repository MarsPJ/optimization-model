import networkx as nx
import matplotlib.pyplot as plt

# 创建一个无向图
G = nx.Graph()

# 批量添加节点
# nodes = ["A", "B", "C", "D", "E", "F"]
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G.add_nodes_from(nodes)

# 批量添加边及其权重
# edges_and_weights = [("A", "B", 4), ("A", "C", 2), ("B", "C", 3),
#                      ("B", "D", 5), ("C", "D", 1), ("D", "E", 7),
#                      ("D", "F", 6), ("E", "F", 8)]
edges_and_weights = [("A", "B", 4), ("A", "C", 2), ("B", "C", 3),
                     ("B", "D", 5), ("C", "D", 1), ("D", "E", 7),
                     ("D", "F", 6), ("E", "F", 8), ("E", "G", 9),
                     ("F", "G", 3), ("G", "H", 2), ("H", "I", 5),
                     ("I", "J", 4), ("J", "A", 6), ("B", "I", 1),
                     ("C", "H", 3), ("D", "J", 2), ("E", "I", 7),
                     ("F", "H", 4), ("G", "J", 8)]
G.add_weighted_edges_from(edges_and_weights)

# 使用Kruskal算法求解最小生成树
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
"""
可选算法：
'kruskal', 'prim', or 'boruvka'. 
默认：'kruskal'.
"""
# 输出MST的连接情况
print("Minimum Spanning Tree edges:")
for edge in mst.edges(data=True):
    u, v, weight = edge
    print(f"{u} - {v}, Weight: {weight['weight']}")

# 可视化原图和最小生成树
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10, font_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
nx.draw_networkx_edges(mst, pos, edge_color='r', width=2)
plt.title("Graph and Minimum Spanning Tree")
plt.show()
