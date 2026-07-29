"""
Author: Jose David Vera

Purpose: Create a shopping cart program where users can add, view, remove, and manage items.

Creativity: Added a shopping cart item counter and an empty cart message to provide a more user-friendly shopping experience.
"""
print("Welcome to the Shopping Cart Program! ")
print()
menu_items = ["Add item", "View cart", "Remove item", "Compute total", "Quit"] 
cart_items = [] 
price_list = []
action_number = 0
while action_number != 5:
    print("\nPlease select one of the following:")
    for i in range(len(menu_items)):
        menu_option = menu_items[i]
        print(f" {i+1} . {menu_option} ")
    action_number = int(input("Please enter an action: "))
    if action_number == 1:
        item_name = str(input("What item would you like to add? "))
        cart_items.append(item_name)
        item_price = float(input(f"What is the price of {item_name}? "))
        price_list.append(item_price)

    elif action_number == 2:
        if len(cart_items) == 0:
            print("Your shopping cart is empty. Start adding some items!")
        else:    
            print("The contents of the shopping cart are: ")
            print(f"You have {len(cart_items)} item(s) in your cart:")
            for j in range(len(cart_items)):
                item = cart_items[j]
                print(f"{j+1}. {item} - ${price_list[j]:.2f}")

    elif action_number == 3:  
        print("The contents of the shopping cart are: ")
        for j in range(len(cart_items)):
            item = cart_items[j]
            print(f"{j+1}. {item} - ${price_list[j]}")
            
        remove = int(input("\nWhich item would you like to remove?"))
        remove = remove - 1
        if remove >= len(cart_items):
            print("Sorry,you have made an invalid choice")
        else:
            cart_items.pop(remove)
            price_list.pop(remove)
            print("Item removed.")

    elif action_number == 4:
       total = sum(price_list)
       print(f"The total price of the items in the shopping cart is ${total:.2f}")
       print()

print("--------------------")
print("Thank you. Goodbye.")
print("--------------------")
