
"""
在输油管网中，通过输油管连接生产石油的油井、储存石油的油库和转运的中间泵站。各站点之间的连接及管路的容量如图
（参见 2.6 程序运行结果图）所示，求从油井到油库的最大流量和具体方案。
c=最大容量
f=最优解的流量
"""
import matplotlib.pyplot as plt # 导入 Matplotlib 工具包
import networkx as nx  # 导入 NetworkX 工具包

# 1. 最大流问题 (Maximum Flow Problem，MFP)
# 创建有向图
G1 = nx.DiGraph()  # 创建一个有向图 DiGraph
G1.add_edge('s', 'a', capacity=6)  # 添加边的属性 "capacity"：最大容量
G1.add_edge('s', 'c', capacity=8)
G1.add_edge('a', 'b', capacity=3)
G1.add_edge('a', 'd', capacity=3)
G1.add_edge('b', 't', capacity=10)
G1.add_edge('c', 'd', capacity=4)
G1.add_edge('c', 'f', capacity=4)
G1.add_edge('d', 'e', capacity=3)
G1.add_edge('d', 'g', capacity=6)
G1.add_edge('e', 'b', capacity=7)
G1.add_edge('e', 'j', capacity=4)
G1.add_edge('f', 'h', capacity=4)
G1.add_edge('g', 'e', capacity=7)
G1.add_edge('h', 'g', capacity=1)
G1.add_edge('h', 'i', capacity=3)
G1.add_edge('i', 'j', capacity=3)
G1.add_edge('j', 't', capacity=5)

# 求网络最大流
# maxFlowValue = nx.maximum_flow_value(G1, 's', 't')  # 求网络最大流的值
# maxFlowValue, maxFlowDict = nx.maximum_flow(G1, 's', 't')  # 求网络最大流
from networkx.algorithms.flow import edmonds_karp  # 导入 edmonds_karp 算法函数
maxFlowValue, maxFlowDict = nx.maximum_flow(G1, 's', 't', flow_func=edmonds_karp)  # 求网络最大流

# 数据格式转换
edgeCapacity = nx.get_edge_attributes(G1, 'capacity')
edgeLabel = {}  # 边的标签
for i in edgeCapacity.keys():  # 整理边的标签，用于绘图显示
    edgeLabel[i] = f'c={edgeCapacity[i]:}'  # 边的容量
edgeLists = []  # 最大流的边的 list
for i in maxFlowDict.keys():
    for j in maxFlowDict[i].keys():
        edgeLabel[(i, j)] += ',f=' + str(maxFlowDict[i][j])  # 取出每条边流量信息存入边显示值
        if maxFlowDict[i][j] > 0:  # 网络最大流的边（流量>0）
            edgeLists.append((i,j))

# 输出显示
print("最大流值: ", maxFlowValue)
print("最大流的途径及流量: ", maxFlowDict)  # 输出最大流的途径和各路径上的流量
print("最大流的路径：", edgeLists)  # 输出最大流的途径

# 绘制有向网络图
fig, ax = plt.subplots(figsize=(8, 6))
pos = {'s': (1, 8), 'a': (6, 7.5), 'b': (9, 8), 'c': (1.5, 6), 'd': (4, 6), 'e': (8, 5.5),  # 指定顶点绘图位置
       'f': (2, 4), 'g': (5, 4), 'h': (1, 2), 'i': (5.5, 2.5), 'j': (9.5, 2), 't': (11, 6)}
# pos=nx.spectral_layout(G1)
# 可以使用内置的生成坐标算法,常见的如下：
"""
networkx.drawing.layout.spring_layout：这是一种基于弹簧模型的布局算法。它模拟了带有弹簧和斥力的物理系统，将节点排斥开，并将边吸引在一起。它通常适用于非常大的图，以及需要节点之间保持一定距离的情况。
networkx.drawing.layout.circular_layout：这种布局将节点均匀分布在一个圆上，适用于环形图或需要显示循环关系的图。
networkx.drawing.layout.spectral_layout：这是基于图的谱分解的布局算法。它利用了图的特征向量来排列节点，适用于图的拓扑结构较为复杂的情况。
networkx.drawing.layout.kamada_kaway_layout：这个布局算法旨在最小化节点之间的路径长度，适用于中等大小的图。
networkx.drawing.layout.shell_layout：这种布局将节点排列在多个同心圆上，适用于具有层次结构的图。
networkx.drawing.layout.random_layout：这个布局算法会随机地将节点放置在一个区域内，适用于快速查看图的大致结构。
"""
edge_labels = nx.get_edge_attributes(G1, 'capacity')
ax.set_title("Maximum flow of petroleum network with NetworkX")  # 设置标题
nx.draw(G1,  pos, with_labels=True, node_color='c', node_size=300, font_size=10)  # 绘制有向图，显示顶点标签
nx.draw_networkx_edge_labels(G1, pos, edgeLabel, font_color='navy')  # 显示边的标签：'capacity' + maxFlow
nx.draw_networkx_edges(G1, pos, edgelist=edgeLists, edge_color='m')  # 设置指定边的颜色、宽度
plt.axis('on')  # Youcans@XUPT
plt.show()
