class Node:
    def __init__(self,data):
        self.data=data
        self.left_child=None
        self.right_child=None

class BST:
    def __init__(self):
        self.root=None

    def __str__(self):
        if(self.root ==None):
            return "Root is Empty"
        else:
            return str(self.root.data)

    def addNode(self, node):
        if self.root == None:
            self.root = node
        elif self.root.data == node.data:
            print("Node already exists")
        else:
            self.addToRoot(node,self.root)

    def addToRoot(self,node,root):
        if node.data<root.data:
            if root.left_child == None:
                root.left_child=node
            else:
                self.addToRoot(node,root.left_child)
        else:
            if root.right_child == None:
                root.right_child=node
            else:
                self.addToRoot(node,root.right_child)

    def printPreOrder(self):
        if self.root == None:
            print("Tree is empty", end=" ")
        else:
            print("\nPre order tree: \n--------------")
            self._printPreOrder(self.root)

    def _printPreOrder(self,root):
        if root !=None:
            print(str(root.data), end=" ")
            self._printPreOrder(root.left_child)
            self._printPreOrder(root.right_child)


    def printInOrder(self):
        if self.root == None:
            print("Tree is empty", end=" ")
        else:
            print("\nIn order tree: \n--------------")
            self._printInOrder(self.root)

    def _printInOrder(self,root):
        if root !=None:
            self._printInOrder(root.left_child)
            print(str(root.data), end=" ")
            self._printInOrder(root.right_child)

    def printPostOrder(self):
        if self.root == None:
            print("Tree is empty", end=" ")
        else:
            print("\nPost order tree: \n--------------")
            self._printPostOrder(self.root)

    def _printPostOrder(self,root):
        if root !=None:
            self._printPostOrder(root.left_child)
            self._printPostOrder(root.right_child)
            print(str(root.data), end=" ")

    def getNumberofNodes(self):
        if self.root == None:
            print("Tree is empty", end=" ")
        else:
            self.count = 0
            self._getNumberofNodes(self.root)
            print("\n\nNumber of nodes in the BST:",self.count)

    def _getNumberofNodes(self,root):
        if root !=None:
            self.count = self.count+1
            self._getNumberofNodes(root.left_child)
            self._getNumberofNodes(root.right_child)

def main():
    myBST = BST()
    print(myBST)

    myNode = Node(8)
    myBST.addNode(myNode)
    myNode = Node(8)
    myBST.addNode(myNode)
    myNode = Node(10)
    myBST.addNode(myNode)
    myNode = Node(9)
    myBST.addNode(myNode)
    myNode = Node(5)
    myBST.addNode(myNode)
    myNode = Node(3)
    myBST.addNode(myNode)
    myNode = Node(4)
    myBST.addNode(myNode)
    myBST.printPreOrder()
    myBST.printInOrder()
    myBST.printPostOrder()
    myBST.getNumberofNodes()


main()
