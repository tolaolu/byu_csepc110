menuList = ["Add a new item", "Display the contents of the shopping cart", "Remove an item", "Compute the total", "Quit"]
userInput = ""
ShoppingCart = []  # Stores items as (name, price) tuples

print("Welcome to the Shopping Cart Service! \n"
      "=====================================")

while userInput != 5:
    print("\nPlease Select an option from the Menu below: \n"
          "===========Options=====================\n"
          "Press 1 to add a new item, 2 to display the contents of the shopping cart  \n"
          "3 to remove an item, 4 to compute the total, or 5 to quit.\n"
          "============Menu==================")
    for i in range(len(menuList)):
        print(f"{i + 1}. {menuList[i]}")
    
    try:
        userInput = int(input().strip()) # Ensure user input is a clean integer
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue
    
    if userInput == 1:
        print("You entered 1 to 'Add a new item'.")
        itemName = input("Item name: ").strip()
        
        try:
            itemPrice = float(input(f"What is the price for '{itemName}'?: ").strip())
            ShoppingCart.append((itemName, itemPrice)) 
            print(f"'{itemName}' has been added to the cart. \n"
                  "======================================\n")
        except ValueError:
            print("Invalid price format. Item not added.")
    
    elif userInput == 2:
        print("You entered 2 to 'Display the contents of the shopping cart'.")
        if not ShoppingCart:
            print("Your shopping cart is empty.")
        else:
            print("The contents of the shopping cart are:")
            for index, (name, price) in enumerate(ShoppingCart, start=1):
                print(f"{index}. {name} - ${price:.2f}")
            
    elif userInput == 3:
        print("You entered 3 to 'Remove an item'.")
        if not ShoppingCart:
            print("Your cart is already empty.")
        else:
            print("The contents of the shopping cart are:")
            for index, (name, price) in enumerate(ShoppingCart, start=1):
                print(f"{index}. {name} - ${price:.2f}")
            itemToRemove = input("Which item would you like to remove?: ").strip()
            try:
                itemIndex = int(itemToRemove) - 1
                if 0 <= itemIndex < len(ShoppingCart):
                    removedItem = ShoppingCart.pop(itemIndex)
                    print(f"'{removedItem[0]}' has been removed from the cart. \n"
                          "======================================\n")
                else:
                    print("Sorry, that is not a valid item number.")
            except ValueError:
                print("Sorry, that is not a valid item number.")
            
    elif userInput == 4:
        print("You entered 4 to 'Compute the total'.")
        totalPrice = sum(item[1] for item in ShoppingCart) if ShoppingCart else 0.0
        print(f"The total price of items in the cart is: ${totalPrice:.2f}")
        print("======================================\n")

    elif userInput == 5:
        print("You entered 5 to 'Quit'.")
        print("Thank you. Goodbye!")
    else:
        print("Invalid selection. Please try again.")