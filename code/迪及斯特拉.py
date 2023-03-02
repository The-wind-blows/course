import sys
max = sys.maxsize

vertices_number = 6
adjacency_matrix = [
    [0, 1, 10, 1, 3, 2],
    [10, 0, 1, 7, 5, 1],
    [1, 10, 0, 6, 1, 1],
    [1, 3, 2, 0, 1, 10],
    [1, 5, 2, 10, 0, 1],
    [1, 2, 1, 6, 10, 0]]
start = []
dest = ["2", "5"]
distance = []


def init_distances(s: int):
    # 初始化所有顶点到源的距离
    global distance
    distance = [max] * vertices_number
    distance[s] = 0


def dijkstra(from_vertex, dest_vertex):
    # 首先轮流更新所有顶点获得hop_path, 再从hop_path中取得对应路径
    star = int(from_vertex) - 1
    des = int(dest_vertex) - 1
    init_distances(star)
    mark = [star]  # 这个就是标记,最先标记目标点的索引
    current_vertex = star  # 当前所在顶点的索引
    hop_path = {}

    # 更新和标记所有顶点
    while len(mark) <= vertices_number and current_vertex != des:
        # 先计算其余顶点到当前顶点current_vertex的距离， 然后把该顶点索引标记，把到当前顶点最近的索引更新为下一个顶点
        for i in range(vertices_number):
            if i != current_vertex and i not in mark and \
                    adjacency_matrix[current_vertex][i] > 0 \
                    and distance[i] > adjacency_matrix[current_vertex][i]:
                distance[i] = distance[current_vertex] + \
                    adjacency_matrix[current_vertex][i]
                hop_path.update(
                    {i + 1: {"from": current_vertex + 1, "cost": adjacency_matrix[current_vertex][i]}})

        if current_vertex not in mark:
            mark.append(current_vertex)

        current_vertex = des
        for i in range(vertices_number):
            if i not in mark and distance[i] < distance[current_vertex]:
                current_vertex = i
    # 倒序找出最短路径
    if len(hop_path) == 0 or int(dest_vertex) not in hop_path:
        return -1, -1
    else:
        current_des = int(dest_vertex)
        path_str = str(dest_vertex)
        while(True):
            current_dic = hop_path.get(current_des, None)
            if(current_dic == None):
                break
            cost = hop_path[current_des]["cost"]
            current_des = hop_path[current_des]["from"]
            path_str = str(current_des) + \
                "  -(" + str(cost) + ")-  " + path_str
        print(distance)
        return distance[des], path_str


cost, path = dijkstra(1, 5)
print("路径长:", cost, "  路径为： ", path)
