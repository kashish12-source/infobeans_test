
# Q1. Electricity Bill Calculator — if-elif-else

# Write a Python program to calculate the electricity bill based on the number of units consumed.

# Use the following slab rates:

# Units	Rate
# First 100 units	₹5/unit
# Next 100 units	₹7/unit
# Next 200 units	₹10/unit
# Above 400 units	₹12/unit

# The program should accept the number of units from the user and calculate the total bill.

# Example:

# Enter units: 350
# Electricity Bill: ₹2700
units = int(input("Enter a units here : "))
bill=0
if units<=100:
    bill = units*5
elif units<=200 and units >100:
    bill = 100*5 + (units-100)*7    
elif units<=400 :
    bill = 100*5 + 100*7 + (units-200)*10
else:
    bill = 100*5 + 100*7 + 200*10 + (units-400)*12
print(f"The total electricity bill is : {bill}")
