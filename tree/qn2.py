class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else " "
        print(prefix+self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)

    
def produce_tree():
        root=TreeNode("Global")
        #india
        india=TreeNode("India")
        karnataka=TreeNode("Karnataka")
        gujarat=TreeNode("Gujarat")
        karnataka.add_child(TreeNode("Bangaluru"))
        karnataka.add_child(TreeNode("Mysore"))
        gujarat.add_child(TreeNode("ahamdabad"))
        gujarat.add_child(TreeNode("Baroda"))
        india.add_child(gujarat)
        india.add_child(karnataka)

        #usa
        usa=TreeNode("USA")
        new_jersey=TreeNode("New Jersey")
        new_jersey.add_child(TreeNode("Princeton"))
        new_jersey.add_child(TreeNode("Trenton"))
        califor=TreeNode("California")
        califor.add_child(TreeNode("San Fransisco"))
        califor.add_child(TreeNode("Mountain view"))
        califor.add_child(TreeNode("Palo Alto"))
        usa.add_child(new_jersey)
        usa.add_child(califor)

        root.add_child(india)
        root.add_child(usa)
        return root
    
if __name__ == '__main__':
    root_node = produce_tree()
    print("***Level1***")
    root_node.print_tree(1)
    print("***Level2***")
    root_node.print_tree(2)
    print("***Level3***")
    root_node.print_tree(3)