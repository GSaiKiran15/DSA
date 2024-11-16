class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

my_tree = Node('A', Node('B', Node("D"), Node("E")),
               Node("C", Node("F"), Node("G")))

def dfs(tree, stack = []):
    root = tree
    stack.append(root)
    while stack:
        root = stack.pop(-1)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)

dfs(my_tree)
        
        