# Q3. Lists — Second-Largest Distinct Element (5 Marks)

# Given a list of integers, find the second-largest distinct element without using sort(), sorted(), or max().

# numbers = [12, 45, 7, 45, 30, 22, 30]

# Expected output: 30
num = [12, 45, 7, 45, 30, 22, 30]

for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j] = num[j],num[i]
print(num)
max = num[-1]
for i in range(len(num)-2 , -1 ,-1):
    if num[i]<max:
        print(f"The second largest distinct element is : {num[i]}")
        break

else:
    print("All the elements are same ")