class TreeNode:
    def __init__(self, rootObj):
        self.data = rootObj
        self.leftChild = None
        self.rightChild = None

    # 添加左子树，没有左子树就直接添加，有就把新节点指向左子树，再将根节点的leftChild指向新节点
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    # 添加右子树，没有右子树就直接添加，有就把新节点指向右子树，再将根节点的rightChild指向新节点

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.data = obj

    def getRootVal(self):
        return self.data
