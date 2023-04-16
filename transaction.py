import tabulate

cart = []
    
def add_item():
    while True:
        name_item = input("Enter Your Item : ").lower()
        if name_item.isnumeric():
            print("Please input your item name.")
        else:
            break

    while True:
        try:
            qt_item = int(input("Enter Quantity : "))
            break
        except ValueError:
            print("Please input the correct quantity.")

    while True:
        try:
            price_item = float(input("Enter Item Price : "))
            break
        except ValueError:
            print("Please input the correct price.")

    item_id = len(cart) + 1

    total_price = qt_item * price_item

    cart.append({
        'No' : item_id,
        'Item' : name_item,
        'Quantity' : qt_item,
        'Total Price' : total_price
    })

    print(">>Item added to your cart<<")

def show_item():
    if not cart:
        print("There is no item in your cart")
    else:
        print(tabulate.tabulate(cart, headers='keys', tablefmt='grid'))

def delete_item():
    print(tabulate.tabulate(cart, headers='keys'))
    no_item = int(input("Enter number to delete : "))

    for i, name_item in enumerate(cart):
        if name_item['No'] == no_item:
            cart.remove(name_item)

            for j in range(i, len(cart)):
                cart[j]['No'] -= 1
            break
    print(tabulate.tabulate(cart, headers='keys'))

def update_item():
    print(tabulate.tabulate(cart, headers='keys'))
    while True:
        try:
            no_item = int(input("Enter number to update : "))
            break
        except ValueError:
            print("Invalid. Please enter the correct number")
    
    new_item = input("Enter New Item : ")

    for name_item in cart:
      if name_item['No'] == no_item:
          name_item['Item'] = new_item
          break
      
    print("You are successfully updated your item")

def update_price():
    print(tabulate.tabulate(cart, headers='keys'))
    while True:
        try:
            no_item = int(input("Enter number to update : "))
            break
        except ValueError:
            print("Invalid. Please enter the correct number")
    
    new_price = input("Enter New Price : ")

    for name_item in cart:
      if name_item['No'] == no_item:
          name_item['Total Price'] = new_price
          break
      
    print("You are successfully updated your item")

def update_qt():
    print(tabulate.tabulate(cart, headers='keys'))
    while True:
        try:
            no_item = int(input("Enter number to update : "))
            break
        except ValueError:
            print("Invalid. Please enter the correct number")
    
    new_qt = input("Enter New Quantity : ")

    for name_item in cart:
      if name_item['No'] == no_item:
          name_item['Quantity'] = new_qt
          break
      
    print("You are successfully updated your item")

def payment_price():
    total_price = 0
    for name_item in cart:
        total_price += name_item['Quantity'] * name_item['Total Price']

    discount = 0

    # Discount percentage based on total_price
    if total_price > 500000:
        discount = 0.1
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05
    
    disc_amount = total_price * discount
    disc_price = total_price - disc_amount

    print(f"Total Price : Rp.{total_price}")
    print(f"Discount : {discount * 100}%")
    print(f"Discounted Price : Rp.{disc_price}")

    # User doing payment for their items
    
    while True:
        try:
            payment = float(input("Enter Payment Amount : "))
        except ValueError:
            print("Error.")
            print("Please enter a number")
            continue

        change = payment - disc_price
        if payment < disc_price:
            print("Please enter the correct amount!")
        elif payment == disc_price:
            print("Thank you!")
            print("See you next time!")
        elif payment > disc_price:
            print(f"Changes: Rp.{change}")
        else:
            break

# Reset option. Used if user want to reset/delete their cart/items 
def reset_item():
    confirmation = input("Are you sure you want to delete cart? (Y/N)").lower

    if confirmation == 'y':
        cart.clear()
        print(">>>All items in your cart is cleared<<<")
    else:
        print(">>>Cancelled<<<")