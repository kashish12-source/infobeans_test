# Q5. Student Result Menu — match-case + loops + if-else

# Write a menu-driven Python program for managing the result of N students.

# The program should repeatedly display:

# 1. Enter student marks
# 2. Display average marks
# 3. Display highest marks
# 4. Display lowest marks
# 5. Display result
# 6. Exit

# Use match-case for menu selection.

# For each student, marks are entered for:

# Python
# Database
# Programming

# A student passes only if:

# Marks in each subject >= 40
# Overall percentage >= 50

# For the Display Result option, print:

# Student 1: Pass
# Student 2: Fail
# Student 3: Pass

# The menu should continue until the user selects 6. Exit.

print("Select the no. from the given menue: ")
print("Press 1 : to enter student marks")
print("Press 2 : to get the average of the marks ")
print("Press 3 : to get the highest marks ")
print("Press 4 : to get the Lowest marks ")
print("Press 5 : to get the Result ")
print("Press 6 : to exit")

average = 0
highest = 0
lowest = 0
result = ""
name =""
n = int(input("Enter here : "))
f = True

while(f):
    if n>=1 and n<=6:
        match n:
            case 1 :
                print("Enter the marks here : ")
                Python = int(input("Enter the marks of Python here : "))
                Database = int(input("Enter the marks of database here : "))
                programming = int(input("Enter the marks of programming here : "))
                sum = Python+Database +programming
                average = sum/3
                if Python > Database and Python>programming:
                    name = "python"
                    highest = Python
                elif Database > programming:
                    name = "database"
                    highest = Database
                else:
                    highest = programming
                    name = "programming"
                if Python < Database and Python<programming:
                    lowest = Python
                    name = "python"
                elif Database < programming:
                    lowest=Database
                    name = "database"
                else:
                    name = "programming"
                    highest = programming
                percentage = sum/3
                if ((Python and Database and programming )>=40 )and percentage >=50:
                    result ="pass"
                else:
                    result = "Fail"
                
            case 2:
                if average !=0:
                    print(f"Average of the marks of the student is : {average:.2f }")
                else:
                    print("You cannot get the average without enter the marks")
                    f = False
            case 3:
                if highest!=0:
                    print(f"Highest marks is in {name} : {highest}  ")
                else:
                    print("You cannot get the Highest without enter the marks")
                    f = False
            case 4:
                if lowest!=0:
                    print(f"Lowest marks is in {name} : {lowest}")
                else:
                    print("You cannot get lowest without enter the marks ")
                    f =False
            case 5:
                if result !="":
                    print(f"Student is : {result}")
                else:
                    print("You cannot get teh result without marks ")
                    f = False
            case 6: 
                f = False 


    else :
        print("You cannot get the average of result without entering the marks of the student ")
        f = False 