class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 
def printInorder(root):
 
    if root:
        printInorder(root.left)
        print(root.val, end=" "),
        printInorder(root.right)
 
 
# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.right = Node(6)
    root.left.right = Node(5)
 
    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root)