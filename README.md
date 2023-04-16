# Super Cashier
This is **Pacmann Final Project** for Python module.

## Program Description
Cashier system program that allows customer to input their item, add quantity, and price for each items. There are options for customer to checkout the items (by calculating the price with quantity) or exit the program. It allows the custome to input and pay by themself (self-service).
This program also generate random Transaction ID for each customer.
## Requirements
1. Create simpe self-service cashier using Python
2. Apply OOP
3. Apply PEP8 principal to create clean Python program
5. Write documentation for each function/method
## Flowchart
1. User input their _Name_ and program will show generated _Transaction ID_ for each customer.
2. User can do several things in this program:
  - Add Item: Customer can add items to the cart
  - Update Item: Customer can update the name of items, quantity, or price of existing item
  - Delete Item: Customer can delete/remove an/several items from their cart
  - Show All Items: Program shows all items that added by customer
  - Reset Item: Customer can reset/delete all the items from their cart
  - Calculate Total Price: Program will calculate all the items in the cart by the price and customer will get discount if Total Price reach certain value.
    - Total Price > Rp.500,000 discount 10%
    - Total Price > Rp.300,000 discount 8%
    - Total Price > Rp.200,000 discount 5%
## Code
**Start program** (main.py)
1. Program will greet user and ask for their name
2. Program will generate custom Transaction ID for each user
3. Program will show user their Name, Transaction ID, and time
4. Program will ask user to input their Item
5. Program branching. Program will ask user if they want to add more items to their cart or continue
6. User can update (edit) their items in their cart
7. User can remove choosen items OR reset their cart
8. User can continue by Checking Out and doing payment
9. If condition meets, user can finish their shopping and program will say thank you and goodbye to user.

## Conclusion
Code used in this program allows customer to add, remove, update, and view their items in the list. User can see the Total Price of their items (+discounted price if meets certain value) or Exit the program.

## Future Works
1. Programmer can identified soecifically for each customer so their Transaction ID is same whenever the customer purchase from Supermarket Andi
2. Create a database for Transaction History/past transaction based on their Transaction ID
3. Create a Search Bar that allows customer to check the price first before checking out the items
