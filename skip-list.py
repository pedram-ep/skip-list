from random import randint, seed

class Node:  
    def __init__(self, height = 0, value = None):
        self.element = value
        self.next = [None]*height

class SkipList:
    def __init__(self):
        self.head = Node()
        self.list_length = 0
        self.maximum_height = 0

    def __len__(self):
        return self.list_length

    def find(self, value, update = None):
        if update == None:
            update = self.update_list(value)
        if len(update) > 0:
            item = update[0].next[0]
            if item != None and item.element == value:
                return item
        return None
    
    def contains(self, value, update = None):
        return self.find(value, update) != None

    def height_generator(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def update_list(self, value):
        update = [None]*self.maximum_height
        x = self.head
        for i in reversed(range(self.maximum_height)):
            while x.next[i] != None and x.next[i].element < value:
                x = x.next[i]
            update[i] = x
        return update
        
    def insert(self, value):
        _node = Node(self.height_generator(), value)

        self.maximum_height = max(self.maximum_height, len(_node.next))
        while len(self.head.next) < len(_node.next):
            self.head.next.append(None)

        update = self.update_list(value)            
        if self.find(value, update) == None:
            for i in range(len(_node.next)):
                _node.next[i] = update[i].next[i]
                update[i].next[i] = _node
            self.list_length += 1

    def add_list(self, unsorted_list):
        for i in range(len(unsorted_list)):
            self.insert(unsorted_list[i])

    def remove(self, value):
        update = self.update_list(value)
        x = self.find(value, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maximum_height -= 1
            self.list_length -= 1            

    def display_list(self):
        x = self.head
        while x.next[0] is not None:
            print(x.next[0].element, end=" ")
            x = x.next[0]
        print('')

    def is_empty(self):
        return self.head.next[0] is None

def input_handling():
    a = 1
    the_skip_list = SkipList()

    while a != 0:
        a = input(
        """Enter one of the following actions:
            1 - Add all of elements of an unsorted list to the skip list
            2 - Add an item to the skip list
            3 - Find an item in the skip list
            4 - Remove the given item from the skip list
            5 - Display the skip list
            
            0 - End the program\n""")
        
        match a:
            case "0":
                print("goodbye!")
                return
            case "1":
                print("Enter a list of numbers separated by spaces:")
                input_list = list(map(int, input().split()))
                the_skip_list.add_list(input_list)
                print("The given elements were added to the skip list successfully")
            
            case "2":
                input_item = int(input("Enter a number: "))
                the_skip_list.insert(input_item)
                print("The new item were added to the skip list successfully.")
            
            case "3":
                input_item = int(input("Enter a number to search in the skip list: "))
                the_answer = the_skip_list.find(input_item)
                if the_skip_list.is_empty is None:
                    print("The skip list is empty")
                elif the_answer == None:
                    print("There wasn't such an item in the skip list.")
                else:
                    print(f"There is an item equal to {the_answer.element}.")
                
            case "4":
                input_item = int(input("Enter a number to remove from the skip list: "))
                if the_skip_list.is_empty is None:
                    print("The skip list is empty")
                elif the_skip_list.find(input_item) == None:
                    print("There wasn't such an item in the skip list")
                else:
                    the_skip_list.remove(input_item)
                    print(f"The item with value of {input_item} is removed from the skip list successfully")
            
            case "5":
                if the_skip_list.is_empty is None:
                    print("The skip list is empty")
                else:
                    the_skip_list.display_list()


input_handling()