class Tree_node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent  = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self


def bst_insert(root, node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root


"""
          10
        /    \
       5      17
      / \    /  \
     3   7  12    19
    / \
   1   4
   """

def create_bst():
    root = Tree_node(10)
    for item in [5, 17, 3, 7, 12, 9, 1, 4]:
        node = Tree_node(item)
        root = bst_insert(root, node)
    return root

def bst_search(node, key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right
    return node

if __name__ == '__main__':
    root = create_bst()
    print(root)
    for key in [7, 8]:
        print('Searching', key)
        print(bst_search(root, key))
