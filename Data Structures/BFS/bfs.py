class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        return "Node(" + str(self.value) + ")"


def bfs(node, queue=list):
    queue.append(node)
    while len(queue) > 0:
        node = queue.pop(0)
        if node is not None:
            print(node)
            queue.append(node.left)
            queue.append(node.right)


my_tree = Node('A', Node('B', Node("D")),
               Node("C", Node("F"), Node("G")))
bfs(my_tree, [])
