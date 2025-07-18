class SimpleNode:  
    def __init__(self, value = None):
        self.element = value
        self.next = None

class SimpleLinkedList:
    """
    Simple linked list for performance comparison
    """
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, value):
        new_node = SimpleNode(value=value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
    
    def contains(self, value):
        current = self.head
        while current:
            if current.element == value:
                return True
            current = current.next
        return False
    
    def remove(self, value):
        if self.head is None:
            return False
        
        if self.head.element == value:
            self.head = self.head.next
            self.length -= 1
            return True
        
        prev = self.head
        current = self.head.next
        while current:
            if current.element == value:
                prev.next = current.next
                self.length -= 1
                return True
            prev = current
            current = current.next
        return False