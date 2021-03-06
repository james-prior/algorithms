
class BinaryNode:
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None
        self.order = []

    def insert(self, root=None, data=None):
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            if root is None:
                root = BinaryNode(data)
            elif data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def pre_order(self, root=None):
        if root:
            self.order.append(root.data)
            if root.left:
                self.pre_order(root.left)
            if root.right:
                self.pre_order(root.right)
        return self.order

    def in_order(self, root=None):
        if root:
            if root.left:
                self.in_order(root.left)
            self.order.append(root.data)
            if root.right:
                self.in_order(root.right)
        return self.order

    def post_order(self, root=None):
        if root:
            if root.left:
                self.post_order(root.left)
            if root.right:
                self.post_order(root.right)
            self.order.append(root.data)
        return self.order
