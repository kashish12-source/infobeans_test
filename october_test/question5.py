# 5. Dictionaries — Word Frequency (5 Marks)

# Write a program to count the frequency of each word in a sentence using a dictionary. Treat uppercase and lowercase words as the same.

# sentence = "Python is easy and Python is powerful"

# Expected output:

# {
#     'python': 2,
#     'is': 2,
#     'easy': 1,
#     'and': 1,
#     'powerful': 1
# }


s ="      Python is easy and Python is powerful"
s= s.strip()
print(s)

l = s.split()

d = {}
for i in l :
    if i in d :
        d[i]+=1
    else:
        d[i]=1

for key,val in d.items():
    print(f"'{key}' : {val}")

