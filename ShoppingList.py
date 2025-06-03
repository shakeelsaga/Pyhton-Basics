print("Welcome to the Shopping List App!\n")

def shopping_list():
    dic = {}
    while True:
        print("Available commands:\n"
              "add - To add an item to the shopping list\n"
              "remove- To remove an item from the shopping list\n"
              "view - To view the current shopping list\n"
              "quit - To exit the app\n")
        
        cmd = input(">").lower()
        if cmd == "add":
            item = input("Enter the item to add: ")
            quantity = input("Enter the quantity: ")
            if item in dic:
                dic[item] += int(quantity)
            else:
                dic[item] = int(quantity)
            print(f"Added {quantity} of {item} to the shopping list.\n")
        elif cmd == "remove":
            if not dic:
                print("Your shopping list is empty. Nothing to remove.\n")
            else:
                item = input("Enter the item to remove: ")
                if item in dic:
                    del dic[item]
                    print(f"Removed {item} from the shopping list.\n")
                else:
                    print(f"{item} is not in the shopping list.\n")
        elif cmd == "view":
            if not dic:
                print("Your shopping list is empty.\n")
            else:
                print("Current shopping list:")
                for item, quantity in dic.items():
                    print(f"{item}: {quantity}")
                print()
        elif cmd == "quit":
            print("Exiting the Shopping List App. Goodbye!\n")
            break
        else:
            print("I don't understand that command. Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    shopping_list()
    print("Thank you for using the Shopping List App!")
