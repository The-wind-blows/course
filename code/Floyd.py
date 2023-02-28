f = float('inf')  # float('inf')表示无穷大

# 准备数据
data = [
    [0, 7, f, 5, f, f, f],
    [7, 0, 8, 9, 7, f, f],
    [f, 8, 0, f, 5, f, f],
    [5, 9, f, 0, 15, 6, f],
    [f, 7, 5, 15, 0, 8, 9],
    [f, f, f, 6, 8, 0, 11],
    [f, f, f, f, 9, 11, 0],
]
path = [[i] * 7 for i in range(7)]

for k in range(7):
    for i in range(7):
        for j in range(7):
            if data[i][j] > data[i][k] + data[k][j]:  # 比较距离的大小
                data[i][j] = data[i][k] + data[k][j]  # 每次都存最小的值
                path[i][j] = k  # 记录中间点


# 定义函数找出x到y的具体路径
def show_trace(x,y):
    trace = []
    def add_trace(x, y):
        global mm
        if x != y:
            add_trace(x, path[x][y])
        return trace.append(y)
    add_trace(x,y)
    trace_str = str(trace)
    trace_str = trace_str.replace(',','-->')
    print(f"从 {x} 到 {y} 的最短路径为: {trace_str}")

for i in data:
    print(i)

show_trace(0,4)  # 求A到E的最短路径
show_trace(0,6)	 # 求A到G的最短路径

#[0, 7, 15, 5, 14, 11, 22]
#[7, 0, 8, 9, 7, 15, 16]
#[15, 8, 0, 17, 5, 13, 14]
#[5, 9, 17, 0, 14, 6, 17]
#[14, 7, 5, 14, 0, 8, 9]
#[11, 15, 13, 6, 8, 0, 11]
#[22, 16, 14, 17, 9, 11, 0]
#从 0 到 4 的最短路径为: [0--> 1--> 4]
#从 0 到 6 的最短路径为: [0--> 3--> 5--> 6]

