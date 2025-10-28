class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedlist:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        # Add an item to the top of the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped = self.top.data
        
        self.top = self.top.next
        self._size -= 1
        return popped

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        # Check if the stack is empty
        return self.top is None

    def size(self):
        # Return the number of items in the stack
        return self._size

    def clear(self):
        # Remove all items from the stack
        self.top = None
        self._size = 0

    def getVal(self):
        current = self.top
        values = []
        while current:
            values.append(current.data)   # keep as raw values, not strings
            current = current.next
        return values
    def __str__(self):
        # Return a string representation of the stack
        result = []
        current = self.top
        while current:
            result.append(str(current.data))
            current = current.next
        return "(top -> " + " -> ".join(result) + ")"