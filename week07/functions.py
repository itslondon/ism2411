# I used AI to help trace and diagnose issues in the sales calculation code.
# I noticed from the beginning that there was a “:” missing at the end of statement
“for sale in sales”. I didn't understand the other two problems until I asked AI
which tells me that my ability to debug is pretty poor. It’s something I need to
work on because it shouldn’t have taken AI to figure out those other two problems
out.
#
# It applies to the specific discount that corresponds with the total. The input is
the price, and the output is whatever discount percentage applies to the range your
price fell in and then the price after the discount. For example, the input is
$100. The discount for numbers 80-100 is 10%. Therefore, the output would be 10%
discount and $90. Yes a colleague could use it without reading the body because the
code is self explanatory.
#
# The AI didn’t help or harm me, it made me realize that I need to go over the
basic functions because I forgot the <= isn’t what I want to do here. But in the
past lab it was so I just applied the logic ”oh since it’s here it must be right”
even though the activity called for fixing a problem. I don’t understand any better
than I did before I am at the same level, I believe practice review on Data camp
will help me.
# --- Exercise 1 ---
# Define calculate
def calculate_tax(price, rate):
return price * rate
# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50
# --- Exercise 2 ---
def apply_discount(price, tier):
if tier == "gold":
return price * 0.85
elif tier == "silver":
return price * 0.90
elif tier == "bronze":
return price * 0.95
else:
return price
# Calling the function
price = 200
tiers = ["gold", "silver", "bronze", "none"]
for tier in tiers:
print(f"{tier}: ${apply_discount(price, tier):.2f}")
# --- Exercise 3 ---
# Write out manually first, then refactor into a function
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")
# Refactor into a function
def final_price(price, tier, tax_rate):
discounted = apply_discount(price, tier)
tax = calculate_tax(discounted, tax_rate)
after_tax = discounted + tax
return after_tax
print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")
# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
total = final_price(price, tier, 0.07)
print(f"Price: ${price:.2f}, Tier: {tier}, Total: ${total:.2f}")
# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]
total = 0
for sale in sales:
# I am adding a plus sign in front of the equal to correct start the count
"total+0"
total += sale
print(f"Total: ${total}")
# I think the bug is in the total; it isn't adding up correctly
count = 0
for sale in sales:
# I am adding a : at the end of the for loop line so it won't produce a syntax
error
count += 1
print(f"Count: {count}")
# I think the bug is in the loop, it is going past the amount of numbers in the
list
i = 0
#I am removing the = sign that was in front of < because none of the sales are
equal to the total sales
while i < len(sales):
print(len(sales))
print(sales[i])
i += 1
# The fix is to make the loop inside of the correct range
# --- Exercise 6 ---
x = 100 # apple # Global
def double_it():
x = 999 # local another apple (not the same apple as above)
return x * 2
print(x)
print(double_it())
print(x)
