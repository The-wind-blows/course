class Node:
    __slots__ = 'prev', 'next', 'val'

    def __init__(self, val):
        self.prev = self.next = None
        self.val = val


class CircularDeque:
    def __init__(self, k):
        self.head = self.tail = None
        self.capacity = k
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        node = Node(value)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head=None
        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.head.val

    def getRear(self):
        return -1 if self.isEmpty() else self.tail.val

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def printDeque(self):
        temp = self.head
        if(temp == None):
            print("空队列")
            return
        while(temp != None):
            print(temp.val)
            temp = temp.next


queue = CircularDeque(3)
print("头结点插入1，结果为：")
queue.insertFront(1)
queue.printDeque()
print("尾结点插入2, 结果为：")
queue.insertLast(2)
queue.printDeque()
print("头结点删除1，结果为：")
queue.deleteFront()
queue.printDeque()
print("尾结点删除2， 结果为：")
queue.deleteLast()
queue.printDeque()
print("最后结果")
queue.printDeque()
