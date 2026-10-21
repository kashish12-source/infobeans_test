# Q2. Loops — Prime Numbers (5 Marks)

# Write a program to print all prime numbers between 1 and 100. Do not use any built-in prime-checking function.

# Expected output: 2, 3, 5, 7, 11, ... 97

def print_prime():
    for i in range(2,101):
        f = True
        for j in range(2,i//2+1):
            if i%j ==0:
                f = False
            
        if f:
            print(i)
        

print_prime()