
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        if self.next:
            return f"{self.data} -> {self.next}"
        else:
            return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_beginning(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
    
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
       
    def append_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        node.next = None
        node.prev = self.tail

        self.tail.next = node
        self.tail = node

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, data):
        pass

    def search(self, data):
        pass

    def is_empty(self):
        pass

    def length(self):
        pass

    def traverse_forward(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

    def traverse_backwards(self):
        current_node = self.tail
        while current_node.prev:
            current_node = current_node.prev

    def __repr__(self):
        pass