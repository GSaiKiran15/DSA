class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_length(self):
        node = self
        level = 0
        while node.parent:
            level += 1
            node = node.parent
        return level

    def log(self, type):
        index = 0
        if type == "name":
            index = 0
        elif type == "designation":
            index = 1
        elif type == "both":
            print("  " * self.get_length() + "|--" +
                  self.data[0], f'({self.data[1]})')
            for i in self.children:
                i.log(type)
            return

        print("  " * self.get_length() + "|--" + self.data[index])
        for i in self.children:
            i.log(type)


def build_management_tree():

    root = TreeNode(("Nipul", "CEO"))

    cto = TreeNode(("Chinmay", "CTO"))
    hr = TreeNode(("Gels", "HR Head"))

    ih = TreeNode(("Vishwa", "Infrastructure Head"))
    ah = TreeNode(("Aamir", "Application Head"))
    rm = TreeNode(("Peter", "Recruitment Manager"))
    pm = TreeNode(("Waqas", "Policy Manager"))

    cm = TreeNode(("Dhaval", "Cloud Manager"))
    ap = TreeNode(("Abhijit", "App Manager"))

    root.add_child(cto)
    root.add_child(hr)

    cto.add_child(ih)
    cto.add_child(ah)

    hr.add_child(rm)
    hr.add_child(pm)

    ih.add_child(cm)
    ih.add_child(ap)

    return root


build_management_tree().log("designation")
