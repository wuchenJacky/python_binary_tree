import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return not (None is self._get(item, self.root))

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode.TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode.TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode.TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if not self.root:
            return None
        res = self._get(key, self.root)
        if res:
            return res.payLoad
        return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
