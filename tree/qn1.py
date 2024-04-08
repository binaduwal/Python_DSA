class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, mode="name"):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else " "

        if mode == "name":
            print(prefix + self.name)
        elif mode == "designation":
            print(prefix + self.designation)
        elif mode == "both":
            print(prefix + self.name + " (" + self.designation + ")")

        if self.children:
            for child in self.children:
                child.print_tree(mode)

def binary_tree():
    root = TreeNode("Nilpul", "CEO")
    node1 = TreeNode("chinmay", "CTO")
    node2 = TreeNode("Vishwa", "Infrastructue Head")
    node3 = TreeNode("Dhaval", "Cloud Manager")
    node4 = TreeNode("Abhijit", "App Manager")
    node5 = TreeNode("Aamir", "Application Manager")
    node6 = TreeNode("Gels", "HR Head")
    node7 = TreeNode("Peter", "Recruitment Manager")
    node8 = TreeNode("Waqas", "Policy Manager")

    root.add_child(node1)
    root.add_child(node6)
    node1.add_child(node2)
    node1.add_child(node5)
    node6.add_child(node7)
    node6.add_child(node8)
    node2.add_child(node3)
    node2.add_child(node4)

    return root

if __name__ == '__main__':
    root_node = binary_tree()
    print("Only name:")
    root_node.print_tree("name")
    print("\nOnly designation:")
    root_node.print_tree("designation")
    print("\nBoth name and designation:")
    root_node.print_tree("both")
