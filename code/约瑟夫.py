
from queue import Queue

def josepRing(nums, m):
    q = Queue()
    for i in nums:
        q.put(i)
    
    while not q.empty():
        for i in range(m-1):
            cur = q.get()
            q.put(cur)     # 重新入队列
        # 淘汰
        print(q.get())

josepRing([1, 2, 3, 4, 5], 5)

