import BinarySearchTree as binaryTree
mytree=binaryTree.BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
print(mytree[6])
print(mytree[2])
for elem in mytree:
    print("{0}".format(mytree[elem]))