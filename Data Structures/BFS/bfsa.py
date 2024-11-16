class Node:
    def __init__(self,value=None, left=None, right=None):
        self.left = left
        self.value = value
        self.right = right
    
tree = Node("A", Node("B", Node("D"), Node("E")), Node("C", Node("F"), Node("G")))

def bfs(tree, queue = []):
    root = tree
    queue.append(root)
    while queue is not None:
        root = queue.pop(0)
        print(root.value)
        queue.append(root.left)
        queue.append(root.right)
        
bfs(tree)