shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def Add_item():
    item = input(f"Enter items to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
def remove_item():
    item = input(f"Enter the item to remove: ")
    if item in  shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from shoping list.")
    else:
        print(f"The item is not found in the shopping list.")
def view_list():
    if shopping_list:
        print(f"\nthis is the current shopping list")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print(f"You don't have a shopping list yet")

def main():
    # shopping_list = []
    while True:
        display_menu()
        choice = input(f"Enter yor choice: ")

        if choice == '1':
            Add_item()
        elif choice=='2':
            remove_item()
        elif choice=='3':
            view_list()
        elif choice=='4':
            print("goodbye!")
            break
        else:
            print(f"you entered an invalid option, please try again")
if __name__ == "__main__":
    main()