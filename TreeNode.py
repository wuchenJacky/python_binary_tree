class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payLoad = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        """
        判断是否包含左节点
        :return:
        """
        return self.leftChild

    def hasRightChild(self):
        """
        是否包含右节点
        :return:
        """
        return self.rightChild

    def isLeftChild(self):
        """
        自己是否为父节点的左节点
        :return:
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """
        自己是否为当前节点的右节点
        :return:
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """
        是否为根节点
        :return: bool
        """
        return not self.parent

    def hasAnyChildren(self):
        """
        是否包含子节点
        :return:bool
        """
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """
        是否左右节点都不为None
        :return:
        """
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payLoad = val
        self.leftChild = lc
        self.rightChild = rc
        if self.leftChild:
            self.leftChild.parent = self
        if self.rightChild:
            self.rightChild.parent = self
