from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1, TreeNode(2), TreeNode(3))
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)


def preorderTraversal(root):
    def preorder(root):
        if not root:
            return
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)
    res = list()
    preorder(root)
    return res


print(preorderTraversal(tree))


def levelOrder(root):
    levelOrder = list()
    if not root:
        return levelOrder
    q = deque([root])
    while q:
        level = list()
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levelOrder.append(level)

    return levelOrder[::1]


print(levelOrder(tree))
