class Vertex:
    # 包含5个基本操作，添加某个顶点连接，获取所有连接，获取顶点自身，获取某边权重，打印所有信息
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    # 定义图类，包含的基本功能有添加顶点，获取某个顶点，获取所有顶点，添加边，是否包含顶点，打印
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def __contains__(self, n):
        return n in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


# 实例化
g = Graph()
for i in range(6):
    g.addVertex(i)
# print(g.vertList)
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
for v in g:
    for w in v.getConnections():
        print("(%s , %s)" % (v.getId(), w.getId()))
