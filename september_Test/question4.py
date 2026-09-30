# Q4. Prime Numbers in a Range — Nested Loops

# Write a Python program that accepts two numbers start and end and prints all prime numbers between them.

# Also display the total number of prime numbers found.

# Example:

# Enter start: 10
# Enter end: 30

# Prime numbers:
# 11 13 17 19 23 29

# Total prime numbers: 6

# Restriction: Do not use any built-in function/library for checking whether a number is prime.

num_1 = int(input("Enter the first no. here : "))
num_2 = int(input("Enter the seconde no. here : "))
count = 0
f = True
for i in range(num_1,num_2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                f=False
                break
        if f:
            print(i,end=" ")
            count+=1
        f=True
    else:
        print(f"{i} is not a prime no.")
