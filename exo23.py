class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_preorder(node):
    if node:
        print(node.value, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)

# Example of constructing a binary tree
def build_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root
