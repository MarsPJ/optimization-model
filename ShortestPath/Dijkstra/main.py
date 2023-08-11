import matplotlib.patches
import networkx as nx
import matplotlib.pyplot as plt

# 创建图并添加节点、边以及权重
G = nx.DiGraph() # Graph表示无向图
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2, {'weight': 2}),
                  (1, 3, {'weight': 4}),
                  (2, 3, {'weight': 1}),
                  (2, 4, {'weight': 7}),
                  (3, 4, {'weight': 3}),
                  (3, 5, {'weight': 5}),
                  (4, 5, {'weight': 2})])

# 指定起始节点和目标节点
source = 1
target = 5

# 使用Dijkstra算法计算最短路径
shortest_path_length, shortest_path = nx.single_source_dijkstra(G, source=source, target=target, weight='weight')
print("Shortest Path Length:", shortest_path_length)
print("Shortest Path:", shortest_path)

# 绘制原始图
pos = nx.spring_layout(G)  # 位置不对劲可以多运行几次
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=10, font_color='black')   # 画点
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}  # data=True 参数允许你访问边的属性字典
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')  # 画边

# 绘制最短路径示意图
shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]  # 生成边集合
arrow_style = '->'  # 设置最短路径示意图箭头风格
"""
 |    Curve          ``-``       None                                                                      
 |    CurveB         ``->``      head_length=0.4, head_width=0.2                                           
 |    BracketB       ``-[``      widthB=1.0, lengthB=0.2, angleB=None                                      
 |    CurveFilledB   ``-|>``     head_length=0.4, head_width=0.2                                           
 |    CurveA         ``<-``      head_length=0.4, head_width=0.2                                           
 |    CurveAB        ``<->``     head_length=0.4, head_width=0.2                                           
 |    CurveFilledA   ``<|-``     head_length=0.4, head_width=0.2                                           
 |    CurveFilledAB  ``<|-|>``   head_length=0.4, head_width=0.2                                           
 |    BracketA       ``]-``      widthA=1.0, lengthA=0.2, angleA=None                                      
 |    BracketAB      ``]-[``     widthA=1.0, lengthA=0.2, angleA=None, widthB=1.0, lengthB=0.2, angleB=None
 |    Fancy          ``fancy``   head_length=0.4, head_width=0.4, tail_width=0.4                           
 |    Simple         ``simple``  head_length=0.5, head_width=0.5, tail_width=0.2                           
 |    Wedge          ``wedge``   tail_width=0.3, shrink_factor=0.5                                         
 |    BarAB          ``|-|``     widthA=1.0, angleA=None, widthB=1.0, angleB=None     
"""
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='red', width=5, arrows=True, arrowsize=25, arrowstyle=arrow_style)  # 在原图画最短路径示意图

plt.show()
