# Q3. Number Analysis — Loop + if-else

# Write a Python program that accepts a positive integer N and prints:

# Sum of all digits
# Number of digits
# Largest digit
# Smallest digit
# Whether the number is a palindrome

# Example:

# Enter number: 12321

# Sum of digits: 9
# Number of digits: 5
# Largest digit: 3
# Smallest digit: 1
# Palindrome: Yes

# Restriction: Do not convert the number into a string.

n =int(input("Enter a positive no. here : "))
sum =0 
count =0
org = n
min=0
max =0
palindrome_check=0
while(n!=0):
    
    dig = n%10
    
    if (dig<min):
        min = dig
    elif dig>max:
        max = dig
        
    count+=1
    
    sum+=dig
    palindrome_check =palindrome_check*10+dig
    n=n//10
print(f"The sum of all the digits is : {sum}")
print(f"The number of digits in n is : {count}")
print(f"The maximum digit is : {max}")
print(f"The minimum digit is : {min}")

if(org ==palindrome_check):
    print("The no. is palindrome")
else:
    print("The no. is not palindrome ")
    