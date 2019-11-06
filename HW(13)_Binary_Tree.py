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

    def printTree(self):
        if self.root == None:
            print("Tree is empty")
        else:
            self.printNode(self.root)

    def printNode(self,root):
        if root !=None:
            self.printNode(root.left_child)
            print(str(root.data))
            self.printNode(root.right_child)

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
    myBST.printTree()

main()
