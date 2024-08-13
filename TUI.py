from skip_list import (SkipList, Node)
# from skip_list import Node


def main():
    input_action = 1
    the_skip_list = SkipList()

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
                print("goodbye!")
                return
            case "1":
                print("Enter input_action list of numbers separated by spaces:")
                input_list = list(map(int, input().split()))
                the_skip_list.add_list(input_list)
                print("The given elements were added to the skip list successfully")
            
            case "2":
                input_item = int(input("Enter input_action number: "))
                the_skip_list.insert(input_item)
                print("The new item were added to the skip list successfully.")
            
            case "3":
                input_item = int(input("Enter input_action number to search in the skip list: "))
                the_answer = the_skip_list.find(input_item)
                if the_skip_list.is_empty is None:
                    print("The skip list is empty")
                elif the_answer == None:
                    print("There wasn't such an item in the skip list.")
                else:
                    print(f"There is an item equal to {the_answer.element}.")
                
            case "4":
                input_item = int(input("Enter input_action number to remove from the skip list: "))
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


main()