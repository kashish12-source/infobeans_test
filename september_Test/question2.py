# Q2. Simple Calculator — match-case

# Write a Python program that accepts:

# Two numbers
# An operator (+, -, *, /, %)

# Use match-case to perform the selected operation.

# The program should also handle division by zero.

# Example:

# Enter first number: 20
# Enter second number: 5
# Enter operator: /

# Result: 4.0

# For an invalid operator:

# Invalid
num_1 = int(input("Enter first no. here : "))
num_2 = int(input("Enter second no. here : "))
print("Chose the operators from the below list :\n+\n-\n*\n/\n%")

operator = input("Enter the operator here : ")

match operator:
    case "+":
        print(f"The addition of two numbers is : {num_1 + num_2}")
    case "-":
        
        print(f"The substraction of two numbers is : {num_1 - num_2}")
        
    case "*":
        print(f"Multiplication of two numbers is : {num_1*num_2}")
    case "/":
        if num_2>0:
            print(f"The division of two numbers is : {(num_1/num_2):.2f}")
        else :
            print(f"The denominators can not be 0")
    case "%":
        if num_2>0:
            print(f"the remider is : {num_1 % num_2 }")
        else:
            print("the denominators can not be 0")
    case _:
        print(f"please choose the valid operator to perform operations ")