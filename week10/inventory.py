# The most surprising thing is I thought I would have to type out the numbers over and over again in order for the code to know what list I'm referring to. But in Python you establish in the very beginning what list it is that you are talking about and then when you type inventory... it will trigger that list instead of you retyping everything out again.
# An internship where I was organizing art into categories such as what school, grade, and type of artwork it was. A python list would have been useful compared to meet manually typing in all of that information. If all of the artworks information would have been typed into python from the very beginning it would be very easy to call on that initial list and make different types of categoriessub lists that my boss required of me.
# Inventory.py
# Author: London Williams
# Module 10 Lab: Inventory List Manager

print( "--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print( "--- Exercise 2: Index Practice ---")
print(inventory[0])  # Print the first item
print(inventory[-1])  # Print the last item
middle = len(inventory) // 2
print(inventory[middle])  # The middle item

print("--- Exercise 3: Slicing Practice ---")
print(inventory[ :3])  #three first items
print(inventory[-2:])  #last two items
print(inventory[::2])  #every other item


print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")  
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -784.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)


print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total/count

print(f"Total sales: ${total}")
print(f"Average: {average}")
print(f"Best: ${max(sales)}")
print(f"Worst: ${min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2))  # 10% discount


print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)


print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: ${sum(high_sales)/len(high_sales):.2f}")




