from Node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        return self.count(self.root)

    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    def insert(self, payload):
        new_node = Node(payload)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if payload < current.payload:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif payload > current.payload:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def delete(self, payload):
        self.root = self.delete1(self.root, payload)

    def delete1(self, node, payload):
        if node is None:
            return None
        if payload < node.payload:
            node.left = self.delete1(node.left, payload)
        elif payload > node.payload:
            node.right = self.delete1(node.right, payload)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self.find_min(node.right)
            node.payload = successor.payload
            node.right = self.delete1(node.right, successor.payload)
        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, payload):
        current = self.root
        while current is not None:
            if payload == current.payload:
                return True
            elif payload < current.payload:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self):
        result = []
        self.inorder1(self.root, result)

    def inorder1(self, node, result):
        if node is None:
            return
        self.inorder1(node.left, result)
        result.append(node.payload)
        self.inorder1(node.right, result)

    def preorder(self):
        result = []
        self.preorder1(self.root, result)
        return result

    def preorder1(self, node, result):
        if node is None:
            return
        result.append(node.payload)
        self.preorder1(node.left, result)
        self.preorder1(node.right, result)

    def postorder(self):
        result = []
        self.postorder1(self.root, result)
        return result

    def postorder1(self, node, result):
        if node is None:
            return
        self.postorder1(node.left, result)
        self.postorder1(node.right, result)
        result.append(node.payload)