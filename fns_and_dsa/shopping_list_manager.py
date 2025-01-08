def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item=str(input("Enter the item to add: ")).lower() # Prompt for and add an item
            shopping_list.append(item)
        elif choice == '2':
            while True:
                item2=str(input("Enter the item to remove: ")).lower() # Prompt for and remove an item
                if item2 in shopping_list:
                    shopping_list.remove(item2)
                    break
                else:
                    print ("This item is not in the shopping list. Please enter the name correctly and try again")
                    continue
        elif choice == '3':
            print (shopping_list)# Display the shopping list
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()