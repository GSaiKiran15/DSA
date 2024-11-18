class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
my_tree = Node('A', Node('B', Node("D")),
               Node("C", Node("F"), Node("G")))

def dfs(tree):
    stack = [tree]
    output = []
    while stack:
        root = stack.pop(-1)
        print(root.value)
        output.append(root.value)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return output

def recursive_dfs(tree):
    if not tree:
        return []
    return [tree.value] + recursive_dfs(tree.left) + recursive_dfs(tree.right)

print(dfs(my_tree))