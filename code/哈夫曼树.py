from collections import deque

class BinaryTree:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.left = None
        self.right = None

def getMin2(li):
    # 定义获取列表中权重最小的两个结点：
    result = [BinaryTree(None, float('inf')), BinaryTree(None, float('inf'))]
    list_new = []
    for i in range(len(li)):
        if li[i].weight < result[0].weight:
            if result[1].weight != float('inf'):
                list_new.append(result[1])
            result[0], result[1] = li[i], result[0]
        elif li[i].weight < result[1].weight:
            if result[1].weight != float('inf'):
                list_new.append(result[1])
            result[1] = li[i]
        else:
            list_new.append(li[i])
    return result, list_new

def makeHuffman(source):
    m2, name = getMin2(source)
    print(m2[0].name, m2[1].name)
    left = m2[0]
    right = m2[1]
    sumLR = left.weight + right.weight
    father = BinaryTree(None, sumLR)
    father.left = left
    father.right = right
    if name == []:
        return father
    name.append(father)
    return makeHuffman(name)

def breadthFirst(gen, index=0, nextGen=[], result=[]):
    # 遍历输出结果
    if type(gen) == BinaryTree:
        gen = [gen]
    result.append((gen[index].name, gen[index].weight))
    if gen[index].left != None:
        nextGen.append(gen[index].left)
    if gen[index].right != None:
        nextGen.append(gen[index].right)
    if index == len(gen)-1:
        if nextGen == []:
            return
        else:
            gen = nextGen
            nextGen = []
            index = 0
    else:
        index += 1
    breadthFirst(gen, index, nextGen, result)
    return result

sourceData = [('a', 5), ('b', 4), ('c', 3), ('d', 8),  ('f', 15), ('g', 2)]
sourceData = [BinaryTree(x[0], x[1]) for x in sourceData]

huffman = makeHuffman(sourceData)
print(breadthFirst(huffman))
