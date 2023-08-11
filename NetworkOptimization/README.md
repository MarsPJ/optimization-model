# 网络流问题

**主要有以下问题：**

- 最大流问题
  - 得到最大流以及流量路径
- 最小费用问题
  - 得到从最小流量到最大流量的各个流量的最小费用、流量路径
- 最小费用最大流问题
  - 得到所有可以得到最大流的解中，费用最小的解（包括最大流、最小费用、流量路径）

**需要的参数**

- 点集
- 边集及其相应的最大容量capacity、每单位容量的花费weight

**最后生成结果图需要确定点的坐标**

- 自己设定（点多的时候很麻烦，但是能自行调整比较美观）

- 采用内置生成坐标算法

  ```
  networkx.drawing.layout.spring_layout：这是一种基于弹簧模型的布局算法。它模拟了带有弹簧和斥力的物理系统，将节点排斥开，并将边吸引在一起。它通常适用于非常大的图，以及需要节点之间保持一定距离的情况。
  networkx.drawing.layout.circular_layout：这种布局将节点均匀分布在一个圆上，适用于环形图或需要显示循环关系的图。
  networkx.drawing.layout.spectral_layout：这是基于图的谱分解的布局算法。它利用了图的特征向量来排列节点，适用于图的拓扑结构较为复杂的情况。
  networkx.drawing.layout.kamada_kaway_layout：这个布局算法旨在最小化节点之间的路径长度，适用于中等大小的图。
  networkx.drawing.layout.shell_layout：这种布局将节点排列在多个同心圆上，适用于具有层次结构的图。
  networkx.drawing.layout.random_layout：这个布局算法会随机地将节点放置在一个区域内，适用于快速查看图的大致结构。
  ```