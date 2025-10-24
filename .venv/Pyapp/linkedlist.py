# Node class
class Node:
    def __init__(self, data):
        self.data = data   # store the data
        self.next = None   # pointer to the next node


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None   # start with an empty list

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:   # if list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:    # traverse to the last node
            last = last.next
        last.next = new_node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def getList(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.data))
            current = current.next
        values.append("None")
        return " -> ".join(values)

    def getval(self):
        current = self.head
        values = []
        while current:
            values.append(current.data)   # keep as raw values, not strings
            current = current.next
        return values

    # Get the length of list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Clear the list
    def clear(self):
        current = self.head
        while current:
            nxt = current.next
            current.next = None  # break the link
            current = nxt
        self.head = None



    # Recursive traversal (collect values)
    def recursive_traverse(self):
        # func inside a func
        def _traverse(node): # this do the recursive
            if not node:
                return []
            return [node.data] + _traverse(node.next)
        return _traverse(self.head)

    # Iterative traversal using a stack
    def iterative_traverse_stack(self):
        if not self.head:
            return []
        stack = []
        result = []
        stack.append(self.head)
        while stack:
            node = stack.pop()
            result.append(node.data)
            if node.next:
                stack.append(node.next)
        return result

    # Recursive reverse
    def recursive_reverse(self):
        def _reverse(node, prev=None):
            if not node:
                return prev
            nxt = node.next
            node.next = prev
            return _reverse(nxt, node)
        self.head = _reverse(self.head)

    # Pop head (for stack-like behavior)
    def pop_head(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val