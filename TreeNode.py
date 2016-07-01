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

    def findMin(self):
        """
        查找最小节点
        :return: 最小节点
        """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def findSuccessos(self):
        succ = None
        if self.hasRightChild():  # 如果有右节点，则查找最小的左节点
            succ = self.rightChild.findMin()
        else:
            if self.parent:  # 没有右节点，并且不为根节点
                if self.isLeftChild():  # 如果本身为父节点的左节点，则返回当前节点的父节点
                    succ = self.parent
                else:
                    """如果本身为父节点的右节点，则设置父节点的右节点为None，防止重复查找
                       同时继续进行查找最小节点，并为父节点设置右节点为当前查找的节点 ？？
                    """
                    self.parent.rightChild = None
                    succ = self.findSuccessos()
                    self.parent.rightChild = succ
        return succ

    def isLeaf(self):
        """
        判断当前节点是否为父子节点
        :return: bool
        """
        return not (self.leftChild or self.rightChild)

    def spliceOut(self):
        if self.isLeaf():  # 如果没有子节点
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():  # 有一个子节点
            if self.hasLeftChild():  # 包含左节点
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
