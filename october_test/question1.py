# Write a program that accepts an integer and checks whether it is a Harshad number.

# A number is a Harshad number if it is divisible by the sum of its digits.

# Example:

# Input: 18

# Output: Harshad Number (18 is divisible by 1 + 8 = 9)

a =int(input("Enter a no. here "))

n =a 
sum =0

while(a!=0):
    dig = a%10
    sum +=dig 
    a = a//10
if n%sum ==0:
    print("The no. is harsad no.")
else:
    print("The no. is not a harsad no.")
