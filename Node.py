class Node:
    def __init__(self, payload):
        self.payload = payload
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        left_val = self.left.payload if self.left else None
        right_val = self.right.payload if self.right else None
        return "Node:\n\tpayload:" + str(self.payload) + "\n\tleft:" + str(left_val) + "\n\tright:" + str(right_val)


