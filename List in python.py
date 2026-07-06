# --------------------------------------------------- LIST IN PYTHON ----------------------------------------------------------

# List is a collection of differnt values or different types of items.

# How to define list??

a = ["Ram", 1, "shyam", 12.5]
b = [1,2,3,4,5]
c = [1,22.5,15,16.5]

"""
a = ["Ram", 1, "shyam", 12.5]
-----------------------------------
|   0    |   1   |    2   |   3   |  ---- Forward indexing
-----------------------------------
|  Ram   |  10   |  shyam | 12.5  |
-----------------------------------
|  -4    |  -3   |   -2   |  -1   |  ---- Backward indexing
-----------------------------------
"""

# list slicing in python
# slicing index
#       a [startindex : end index : step value]

print(a[0])
print(a[1])
print(a[2])
print(a[3])

print("backword indexing")

print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

# ---------------------------------------- Various list operations in python ------------------------------------

# Updating list in python

a = ["Ram", 1, "shyam", 12.5]
print(a[1])
a[1] = "Ramesh"
print(a[1])

# Deleting list in python

a = ["Ram", 1, "shyam", 12.5]
print(a)
del a[1]
print(a)

# List traversal in python

a = ["Ram", 1, "shyam", 12.5]
# first way
for i in a:
    print(i)

# second way
for i in range(len(a)):
    print(a[i])


