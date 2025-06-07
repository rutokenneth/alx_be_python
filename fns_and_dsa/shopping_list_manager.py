def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    shopping_list = []
    while True:
        display_menu() # Show the menu to the user
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            # --- Add Item ---
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: # Ensure the item name is not empty
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            # --- Remove Item ---
            if not shopping_list: # Check if the list is empty first
                print("Your shopping list is already empty. Nothing to remove.")
                continue # Skip to the next loop iteration
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list: # Check if the item exists in the list
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' was not found in your shopping list.")
        elif choice == '3':
            # --- View List ---
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                # Enumerate through the list to display items with numbers
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # --- Exit Application ---
            print("Goodbye! Happy shopping!")
            break # Exit the while loop, ending the program
        else:
            # --- Invalid Choice Handling ---
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
