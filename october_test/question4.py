# Q4. Sets — Common and Unique Elements (5 Marks)

# Given two lists, find:

# Elements common to both lists.

# Elements that appear in either list but not in both.

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]

# Expected output:

# Common elements: {30, 40}
# Unique elements: {10, 20, 50, 60, 70}

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]
if len(list1)<len(list2):
    smallest = list1
    greatest = list2
else:
    smallest = list2
    greatest = list1

inter = []
for i in range(len(smallest)):
    if smallest[i] in greatest:
        inter.append(smallest[i])
print(inter)


x = list1+list2
d ={}
s=[]
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d.keys():
    if d[i] ==1:
        s.append(i)

print(s)

