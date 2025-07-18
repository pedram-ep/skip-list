import time
import random
from array import array
from SkipList import SkipList
from SimpleLinkedList import SimpleLinkedList

class SkipListService:
    def __init__(self):
        self.sl = SkipList()
    
    def terminalUIService(self, visualizerOn=True):
        input_action = 1
        while input_action != 0:
            input_action = input(
            """Enter one of the following actions:
    1 - Add all of elements of an unsorted list to the skip list
    2 - Add an item to the skip list
    3 - Find an item in the skip list
    4 - Remove the given item from the skip list
    5 - Display the skip list

    6 - Testing All Operations
    7 - Time Performance Comparison (vs. Array, Python List, and Linked List)

    8 - Visualizer off/on

    0 - End the program\n""")
            
            match input_action:
                case "0":
                    if visualizerOn:
                        print("This is the final skip list:")
                        self.sl.visualize()
                    print("goodbye!")
                    return
                case "1":
                    print("Enter input_action list of numbers separated by spaces:")
                    input_list = list(map(int, input().split()))
                    self.sl.addList(input_list)
                    print("The given elements were added to the skip list successfully")
                    if visualizerOn:
                        self.sl.visualize()
                
                case "2":
                    input_item = int(input("Enter input_action number: "))
                    self.sl.insert(input_item)
                    print("The new item were added to the skip list successfully.")
                    if visualizerOn:
                        self.sl.visualize()
                
                case "3":
                    input_item = int(input("Enter input_action number to search in the skip list: "))
                    the_answer = self.sl.find(input_item)
                    if self.sl.isEmpty is None:
                        print("The skip list is empty")
                    elif the_answer == None:
                        print("There wasn't such an item in the skip list.")
                    else:
                        print(f"There is an item equal to {the_answer.element}.")
                    
                case "4":
                    input_item = int(input("Enter input_action number to remove from the skip list: "))
                    if self.sl.isEmpty is None:
                        print("The skip list is empty")
                    elif self.sl.find(input_item) == None:
                        print("There wasn't such an item in the skip list")
                    else:
                        self.sl.remove(input_item)
                        print(f"The item with value of {input_item} is removed from the skip list successfully.\n")
                        if visualizerOn:
                            self.sl.visualize()
                
                case "5":
                    if self.sl.isEmpty is None:
                        print("The skip list is empty")
                    else:
                        self.sl.visualize()
                        
                case "6":
                    self.operationsTester(visualizerOn=visualizerOn)

                case "7":
                    numElements = int(input("Enter number of elements for the test: "))
                    if numElements > 1:
                        self.performanceComparison(num_elements=numElements)
                    else:
                        self.performanceComparison()

                case "8":
                    visualizerOn = not visualizerOn

    def operationsTester(self, visualizerOn):
        print("===== Simple Operations Test =====")
        
        print("\nInserting values: 5, 2, 8, 1, 10")
        self.sl.insert(5)
        self.sl.insert(2)
        self.sl.insert(8)
        self.sl.insert(1)
        self.sl.insert(10)
        if visualizerOn:
            self.sl.visualize()
        
        print("\nContains test:")
        print("Contains 5?", self.sl.contains(5))  # True
        print("Contains 3?", self.sl.contains(3))  # False
        print("Contains 10?", self.sl.contains(10))  # True
        
        print("\nRemoving values: 2, 10")
        self.sl.remove(2)
        self.sl.remove(10)
        if visualizerOn:
            self.sl.visualize()
        
        print("\nEdge case tests:")
        print("Remove non-existent 100:", self.sl.remove(100))  # False
        print("Insert duplicate 5:", self.sl.insert(5))  # False (already exists)
        
        if visualizerOn:
            print("\nEmpty skip list visualization:")
            emptySL = SkipList()
            emptySL.visualize()
            del emptySL
        
        print("===== End Simple Operations Test =====")

    def performanceComparison(self, num_elements=10000):
        print(f"\n\n===== Performance Comparison Test ({num_elements} elements) =====")
        random.seed(42)
        test_data = [random.randint(1, 1000000) for _ in range(num_elements)]
        search_data = random.sample(test_data, min(1000, num_elements))
        remove_data = random.sample(test_data, min(1000, num_elements))
        
        # SkipList performance
        sl = SkipList()
        start = time.time()
        for val in test_data:
            sl.insert(val)
        sl_insert_time = time.time() - start
        
        start = time.time()
        for val in search_data:
            sl.contains(val)
        sl_search_time = time.time() - start
        
        start = time.time()
        for val in remove_data:
            sl.remove(val)
        sl_remove_time = time.time() - start
        
        # Python list performance
        py_list = []
        start = time.time()
        for val in test_data:
            py_list.append(val)
        py_list_insert_time = time.time() - start
        
        start = time.time()
        for val in search_data:
            val in py_list
        py_list_search_time = time.time() - start
        
        start = time.time()
        for val in remove_data:
            try:
                py_list.remove(val)
            except ValueError:
                pass
        py_list_remove_time = time.time() - start
        
        # Array performance
        py_array = array('i')
        start = time.time()
        for val in test_data:
            py_array.append(val)
        py_array_insert_time = time.time() - start
        
        start = time.time()
        for val in search_data:
            val in py_array
        py_array_search_time = time.time() - start
        
        start = time.time()
        for val in remove_data:
            try:
                py_array.remove(val)
            except ValueError:
                pass
        py_array_remove_time = time.time() - start
        
        # Simple linked list performance
        sll = SimpleLinkedList()
        start = time.time()
        for val in test_data:
            sll.insert(val)
        sll_insert_time = time.time() - start
        
        start = time.time()
        for val in search_data:
            sll.contains(val)
        sll_search_time = time.time() - start
        
        start = time.time()
        for val in remove_data:
            sll.remove(val)
        sll_remove_time = time.time() - start
        
        # Print results
        print("\nInsertion Performance:")
        print(f"SkipList:     {sl_insert_time:.6f} seconds")
        print(f"Python List:  {py_list_insert_time:.6f} seconds")
        print(f"Array:        {py_array_insert_time:.6f} seconds")
        print(f"Linked List:  {sll_insert_time:.6f} seconds")
        
        print("\nSearch Performance:")
        print(f"SkipList:     {sl_search_time:.6f} seconds")
        print(f"Python List:  {py_list_search_time:.6f} seconds")
        print(f"Array:        {py_array_search_time:.6f} seconds")
        print(f"Linked List:  {sll_search_time:.6f} seconds")
        
        print("\nRemoval Performance:")
        print(f"SkipList:     {sl_remove_time:.6f} seconds")
        print(f"Python List:  {py_list_remove_time:.6f} seconds")
        print(f"Array:        {py_array_remove_time:.6f} seconds")
        print(f"Linked List:  {sll_remove_time:.6f} seconds")

        print("===== End Performance Comparison Test =====")