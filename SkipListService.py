from SkipList import SkipList

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
                    visualizerOn = not visualizerOn