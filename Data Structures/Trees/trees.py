class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        node = self
        while node.parent:
            level += 1
            node = node.parent
        return level

    def log(self):
        print("  " * self.get_level() + "|--" + self.data)
        for i in self.children:
            i.log()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    mobile = TreeNode("Mobile")
    camera = TreeNode("Cameras")

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(camera)

    laptop.add_child(TreeNode("ROG"))
    laptop.add_child(TreeNode("MSI"))
    laptop.add_child(TreeNode("Lenovo"))

    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Apple"))
    mobile.add_child(TreeNode("One Plus"))

    camera.add_child(TreeNode("Sony"))
    camera.add_child(TreeNode("Nikon"))
    camera.add_child(TreeNode("Canon"))

    root.log()

    return root


build_tree()
