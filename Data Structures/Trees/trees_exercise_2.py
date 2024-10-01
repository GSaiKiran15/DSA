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

    def log(self, level):
        if self.get_level() < level+1:
            print("  " * self.get_level() + "|--" + self.data)
            for i in self.children:
                i.log(level)


def build_location_tree():

    root = TreeNode("Global")

    IN = TreeNode("India")
    US = TreeNode("USA")

    GJ = TreeNode('Gujarat')
    KA = TreeNode('Karnataka')
    NJ = TreeNode('New Jersey')
    CA = TreeNode('California')

    AM = TreeNode('Ahmedabad')
    BR = TreeNode('Baroda')
    BG = TreeNode('Bangalore')
    MS = TreeNode('Mysore')
    PT = TreeNode('Princeton')
    TR = TreeNode('Trenton')
    SF = TreeNode('San Francisco')
    MV = TreeNode('Mountain View')
    PA = TreeNode('Palo Alto')

    root.add_child(IN)
    root.add_child(US)

    IN.add_child(GJ)
    IN.add_child(KA)

    US.add_child(NJ)
    US.add_child(CA)

    GJ.add_child(AM)
    GJ.add_child(BR)

    KA.add_child(BG)
    KA.add_child(MS)

    NJ.add_child(PT)
    NJ.add_child(TR)

    CA.add_child(SF)
    CA.add_child(MV)
    CA.add_child(PA)

    return root


build_location_tree().log(2)
