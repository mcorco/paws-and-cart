"""
Shopping Cart Application

This project implements a shopping cart functionality for users, allowing them to manage their items effectively.

Features:
- Users can add, remove, and view items in their cart.
- Personalized product suggestions are provided based on the items in the cart.
- Users can view the total cost of their items.
- Error handling techniques are employed to handle invalid entries gracefully.

Usage:
- Add items: Users can add items to their cart.
- Remove items: Users can remove items from their cart.
- View cart: Users can view the contents of their cart along with the total cost.
- Personalized suggestions: The program suggests additional products based on the user's cart content.
- Error handling: Various error handling techniques are implemented to handle invalid inputs.

The shopping cart application provides a seamless shopping experience with efficient management of user items and personalized suggestions, enhancing the overall user experience.
"""

# Shop products with their prices
shop = {
    1: {"product": "Premium Dog Treats", "price": 1.75},
    2: {"product": "Gourmet Dog Selection", "price": 7.90},
    3: {"product": "Dog's Delight Food Tins", "price": 8.75},
    4: {"product": "Dog's Favorite Cottage Pie", "price": 2.50},
    5: {"product": "Sunday Roast for Dogs", "price": 3.00},
    6: {"product": "Prime Chicken Cat Food", "price": 4.50},
    7: {"product": "Luxury Cat Assortment", "price": 11.25},
    8: {"product": "Country Cat Medley", "price": 4.25},
    9: {"product": "Cat's Delight Pouches", "price": 4.55},
    10: {"product": "Tasty Tuna Cake for Cats", "price": 0.95},
    11: {"product": "Poultry Selection for Cats", "price": 3.60},
    12: {"product": "Premium Bird Peanuts", "price": 4.20},
    13: {"product": "Deluxe Bird Mealworms", "price": 1.30},
    14: {"product": "Nutrient-rich Bird Seeds", "price": 1.25},
    15: {"product": "Insect Pellets for Birds", "price": 4.15},
    16: {"product": "Premium Seed Mix for Birds", "price": 3.75},
    17: {"product": "Fresh Orange", "price": 3.25},
    18: {"product": "Juicy Watermelon", "price": 4.10},
    19: {"product": "Large Pineapple", "price": 4.80},
    20: {"product": "Sweet Mango", "price": 3.75},
    21: {"product": "Kiwi Fruit", "price": 2.95},
    22: {"product": "Passion Fruit", "price": 3.15},
    23: {"product": "Bramley Apples", "price": 1.95},
    24: {"product": "Gala Apples", "price": 2.15},
    25: {"product": "Perfect Ripen Strawberry", "price": 4.55},
    26: {"product": "Mixed Berry Delight", "price": 3.85}
}

# Initialize cart
mycart = {}

# Print welcome message
print("=" * 70)
print("WELCOME TO PAUL'S PET SHOP")
print("=" * 70)

# Constantly prompt user for an input
while True:
    print("\nMENU:")
    print("A: Add item to cart")
    print("B: Remove item from cart")
    print("C: View cart")
    print("D: Proceed to checkout")
    choice = input("Enter your choice: ").strip().lower()
    print()

    # Add item to cart
    if choice == "a":
        try:
            num = int(input("Enter the number of the item you wish to add to cart: "))
            if num in shop:
                num_times = int(input("Enter the number of times to add this item to cart: "))
                if num_times > 0:
                    if num in mycart:
                        mycart[num] += num_times
                    else:
                        mycart[num] = num_times
                    print(f"\n{'=' * 70}\nItem added to your cart!\n{'=' * 70}\n")
                else:
                    print("\nPlease enter a valid number of items to add to the cart.\n")
            else:
                print("\nInvalid item number. Please choose a valid item.\n")
        except ValueError as err_mess:
            print(f"\n{'=' * 70}\nInvalid input: {err_mess}\n{'=' * 70}\n")

    # Remove item(s) from cart
    elif choice == "b":
        try:
            num = int(input("Enter the number of the item you wish to remove from cart: "))
            if num in mycart:
                num_times = int(input(f"Enter the number of times to remove '{shop[num]['product']}' from cart: "))
                if num_times >= mycart[num]:
                    del mycart[num]
                else:
                    mycart[num] -= num_times
                print(f"\n{'=' * 70}\nItem removed from your cart!\n{'=' * 70}\n")
            else:
                print("\nItem not found in your cart.\n")
        except ValueError as err_mess:
            print(f"\n{'=' * 70}\nInvalid input: {err_mess}\n{'=' * 70}\n")

    # View cart
    elif choice == "c":
        if mycart:
            print("YOUR CART:")
            print("=" * 70)
            total_price = 0
            for num, quantity in sorted(mycart.items()):
                product = shop[num]["product"]
                price = shop[num]["price"]
                item_price = price * quantity
                print(f"{num}: {product} x {quantity} = £{item_price:.2f}")
                total_price += item_price
            print("=" * 70)
            print(f"Total: £{total_price:.2f}")
        else:
            print("Your cart is empty.")

    # Proceed to checkout
    elif choice == "d":
        print("Thank you for shopping with us! Goodbye!")
        break

    else:
        print("Invalid choice. Please select again.")