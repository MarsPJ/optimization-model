import networkx as nx
import matplotlib.pyplot as plt

maxn = 120
inf = 1000000000


class Edge:
    def __init__(self):
        self.u = 0
        self.v = 0
        self.w = 0


n = 0
r = 0
edge = [Edge() for _ in range(maxn * maxn)]
dist = [inf] * maxn
pre = [0] * maxn
belong = [-1] * maxn
vis = [-1] * maxn


def edmonds(src):
    global n
    ret = 0
    while True:
        for i in range(n):
            dist[i] = inf
        for i in range(r):
            u = edge[i].u
            v = edge[i].v
            if edge[i].w < dist[v] and u != v:
                pre[v] = u
                dist[v] = edge[i].w

        for i in range(n):
            if i == src:
                continue
            if dist[i] == inf:
                return -1

        scnt = 0
        belong = [-1] * maxn
        vis = [-1] * maxn
        dist[src] = 0

        for i in range(n):
            ret += dist[i]
            v = i
            while vis[v] != i and belong[v] == -1 and v != src:
                vis[v] = i
                v = pre[v]
            if v != src and belong[v] == -1:
                u = pre[v]
                while u != v:
                    belong[u] = scnt
                    u = pre[u]
                belong[v] = scnt
                scnt += 1

        if scnt == 0:
            break

        for i in range(n):
            if belong[i] == -1:
                belong[i] = scnt

        for i in range(r):
            v = edge[i].v
            edge[i].u = belong[edge[i].u]
            edge[i].v = belong[edge[i].v]
            if edge[i].u != edge[i].v:
                edge[i].w -= dist[v]

        n = scnt
        src = belong[src]

    return ret


# Example graph
n = 4
r = 5

edge[0].u = 0
edge[0].v = 1
edge[0].w = 1

edge[1].u = 0
edge[1].v = 2
edge[1].w = 2

edge[2].u = 1
edge[2].v = 3
edge[2].w = 5

edge[3].u = 2
edge[3].v = 3
edge[3].w = 4

edge[4].u = 0
edge[4].v = 3
edge[4].w = 3

src = 0
result = edmonds(src)
print("Minimum cost:", result)

# Create the graph
G = nx.DiGraph()
for i in range(r):
    G.add_edge(edge[i].u, edge[i].v, weight=edge[i].w)

# Find the edges in the minimum spanning tree (MST)
MST_edges = [(edge[i].u, edge[i].v) for i in range(r) if edge[i].w == 0]

# Visualize the graph with MST edges highlighted
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): f"{G[i][j]['weight']}" for i, j in G.edges()})
nx.draw_networkx_edges(G, pos, edgelist=MST_edges, edge_color='r', width=2)
plt.title("Minimum Spanning Tree Example")
plt.show()
