from random import randint

class Node:  
    def __init__(self, height = 0, value = None):
        self.element = value
        self.next = [None] * height

class SkipList:
    def __init__(self):
        self.head = Node(height=1)
        self.listLength = 0
        self.maximumHeight = 1

    def __len__(self) -> int:
        return self.listLength

    def find(self, value, update = None):
        if update == None:
            update = self.updateList(value)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.element == value:
                return item
        return None
    
    def contains(self, value, update = None):
        return self.find(value, update) != None

    def heightGenerator(self):
        height = 1
        while randint(1, 2) != 1 and height < 32:
            height += 1
        return height

    def updateList(self, value):
        update = [None] * self.maximumHeight
        x = self.head

        for i in reversed(range(self.maximumHeight)):
            while i < len(x.next) and x.next[i] is not None and x.next[i].element < value:
                x = x.next[i]
            update[i] = x
        return update
        
    def insert(self, value):
        nodeHeight = self.heightGenerator()

        if nodeHeight > self.maximumHeight:
            self.head.next.extend([None]* (nodeHeight - self.maximumHeight))
            self.maximumHeight = nodeHeight
        
        update = self.updateList(value)

        if update[0].next[0] is None or update[0].next[0].element != value:
            newNode = Node(nodeHeight, value)

            for i in range(nodeHeight):
                if i < len(update[i].next):
                    newNode.next[i] = update[i].next[i]
                    update[i].next[i] = newNode
            self.listLength += 1
            return True
        return False

    def addList(self, unsorted_list):
        for value in unsorted_list:
            self.insert(value=value)

    def remove(self, value):
        if self.isEmpty():
            return False
        
        update = self.updateList(value)
        target = update[0].next[0]

        if target is None or target.element != value:
            return False
        
        for i in range(len(target.next)):
            if i < len(update) and i < len(update[i].next) and update[i].next[i] == target:
                update[i].next[i] = target.next[i]

        while self.maximumHeight > 1 and self.head.next[self.maximumHeight-1] is None:
            self.maximumHeight -= 1
        self.listLength -=1
        return True          

    def displayList(self):
        current = self.head.next[0]
        while current is not None:
            print(current.element, end=" ")
            current = current.next[0]
        print('')

    def isEmpty(self):
        return self.listLength == 0

    def traverseLevelZero(self) -> list:
        nodes = []
        current = self.head.next[0]
        while current is not None:
            nodes.append(current)
            current = current.next[0]
        return nodes

    def visualize(self):
        if self.isEmpty():
            print("SkipList is empty")
            return
        
        base_nodes = [self.head]
        current = self.head.next[0]
        while current is not None:
            base_nodes.append(current)
            current = current.next[0]
        
        node_cols = {}
        node_width = 5
        for idx, node in enumerate(base_nodes):
            node_cols[node] = idx * node_width
        total_width = len(base_nodes) * node_width
        
        rows = []
        for level in range(self.maximumHeight - 1, -1, -1):
            row = [' '] * total_width
            current = self.head
            
            while current is not None:
                if level < len(current.next):
                    col = node_cols.get(current, 0)
                    
                    if level == 0:
                        if current == self.head:
                            label = "H"
                        else:
                            label = str(current.element)
                        start = col + (node_width - len(label)) // 2
                        for i, char in enumerate(label):
                            if start + i < total_width:
                                row[start + i] = char
                    else:
                        if col < total_width:
                            row[col + node_width // 2] = '○'
                    
                    next_node = current.next[level]
                    if next_node is not None and next_node in node_cols:
                        next_col = node_cols[next_node]
                        start = col + node_width // 2 + 1
                        end = next_col + node_width // 2
                        for pos in range(start, end):
                            if pos < total_width:
                                row[pos] = '─'
                        if end < total_width:
                            row[end] = '►'
                    
                    if level < len(current.next):
                        current = current.next[level]
                    else:
                        current = None
                else:
                    current = None
            
            level_label = f"L{level}: "
            rows.append(level_label + ''.join(row))
        
        for row in rows:
            print(row)
        print()