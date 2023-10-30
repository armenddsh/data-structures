
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        if self.next:
            return f"{self.data} -> {self.next}"
        else:
            return f"{self.data}"

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.next = None

    def append_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def append_end(self, data):
        node = Node(data)

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node

    def traverse(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next