class Node:
    def __init__(self, student):
        self.student = student
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.student)
            current = current.next
        return result

    def addFront(self, student):
        new_node = Node(student)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count = self.count + 1

    def addBack(self, student):
        new_node = Node(student)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count = self.count + 1

    def removeFront(self):
        if self.head is None:
            return None
        removed = self.head.student
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.count = self.count - 1
        return removed

    def removeBack(self):
        if self.tail is None:
            return None
        removed = self.tail.student
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self.count = self.count - 1
        return removed

    def search(self, name):
        current = self.head
        while current is not None:
            if current.student.get_name() == name:
                return True
            current = current.next
        return False

    def remove(self, name):
        current = self.head
        while current is not None:
            if current.student.get_name() == name:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.count = self.count - 1
                return True
            current = current.next
        return False
