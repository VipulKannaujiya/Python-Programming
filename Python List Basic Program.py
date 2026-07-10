# 1. Program to find sum of elements of the list.

a = []
size = int(input("How Many Elements You Want to Enter : "))
for i in range(size):
    val = int(input("Enter Number : "))
    a.append(val)

sum = 0
for i in range(size):
    sum = sum + a[i]
print("Sum of list element = ", sum)

# 2. Program to count total number of odd and even numbers in the list.

list1 = [32,43,45,78,37,29]
even = 0
odd = 0
for i in range(6):
    if(list1[i] % 2 == 0):
        even += 1
    else:
        odd += 1
print("Total Even Numbers = ", even)
print("Total Odd Numbers = ", odd)
