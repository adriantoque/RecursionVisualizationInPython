class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item of the stack
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        #Return the top item without removing it.
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
    #   Check if the stack is empty.
        return len(self.items) == 0

    def size(self):
        #Return the number of items in the stack.
        return len(self.items)
    def clear(self) -> None:
        # Remove all items from the stack
        self.items.clear()
    
    def getVal(self):
       
        return self.items


    def __str__(self):
        # Return a string representation of the stack.
        return str(self.items)