
# 初始化一个节点
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.header = None
        self.length = 0

    # 判断链表是否为空,数值使用==比较，对象使用is来判断是否为None即可。
    def is_empty(self):
        if self.header is None:
            return True
        else:
            return False

    # 在链表头部添加结点
    def add_node_from_head(self, node):
        if self.header is None:
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.length += 1
        return self

    # 在链表尾部添加结点
    def add_node_from_behind(self, node):
        current_node = self.header
        if self.is_empty():
            self.add_node_from_head(node)
        else:
            # 一直遍历到尾部结点
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1
        return self

    def add_node_index(self, node, index):
        if self.is_empty():
            self.header = node
            self.length = 1
            return self
        if index > self.length - 1 or index < 0:
            print("超出范围,插入失败!")
            return self
        else:
            current_node = self.header
            count = 0
            while True:
                if current_node is not None:
                    # 最少有2个结点
                    if count == index:
                        print("...找到位置....")
                        if count == 0:
                            # 插入到头结点之前
                            node.next = current_node
                            self.header = node
                        else:
                            # 1. 新节点的next指向当前结点
                            # 2. 上一个节点的next指向新结点
                            node.next = current_node
                            last_node.next = node
                        self.length += 1
                        return self
                    else:
                        count += 1
                        last_node = current_node
                        current_node = current_node.next
                else:
                    # 只有一个头结点
                    node.next = current_node
                    self.header = node
                    self.length += 1
                    return self

    # 删除指定结点
    def removce_node_index(self, index):
        current = self.header
        count = 0
        while current is not None:
            if index == count:
                print("找到指定结点!")
                if index == 0:
                    self.header = current.next
                else:
                    last.next = current.next
                self.length -= 1
                return self
            count += 1
            last = current
            current = current.next
        return self

    # 遍历链表
    def traversing_list(self):
        header_node = self.header
        result = ",data:" + str(header_node.data)
        while header_node.next is not None:
            result = result + "-->" + "data:" + str(header_node.next.data)
            temp = header_node
            header_node = header_node.next
            if temp == header_node:
                return
        print("链表为:", result, ",长度为:" + str(self.length))


if __name__ == '__main__':
    print("初始化一个链表!")
    header = Node(0)
    linked_list = LinkedList()
    linked_list.add_node_index(header, 0)
    linked_list.traversing_list()
    print("在头部添加结点!")
    node0 = Node(1)
    linked_list.add_node_from_head(node0)
    linked_list.traversing_list()
    print("在尾部添加结点!")
    node1 = Node(2)
    linked_list.add_node_from_behind(node1)
    linked_list.traversing_list()
    print("在index=1处添加结点!")
    node2 = Node(3)
    linked_list.add_node_index(node2, 1)
    linked_list.traversing_list()
    print("删除index=1的结点!")
    linked_list.removce_node_index(1)
    linked_list.traversing_list()