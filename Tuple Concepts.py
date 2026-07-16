# Differnce 1
list1 = [1,2,3,"ram","shyam"]
tuple1 = (1,2,3,"ram","shyam")

# Differnce 2 : the list is mutable whereas tuples are immutable.

list1 = [1,2,3,"ram", "shyam"]
list1[2] = 10
print(list1)

tuple1 = (1,2,3,"ram","shyam")
#tuple1[2] = 10     ERROR! because tuples are immutable.
print(tuple1)

# Difference 3 : list occupies more memory space as compared that tuple.

import sys

list2 = [1,2,3,"ram", "shyam", "true", "ravi"]
tuple2 = (1,2,3,"ram", "shyam", "true", "ravi")

print("Size of list = ", sys.getsizeof(list2))
print("Size of tuple = ", sys.getsizeof(tuple2))

# Differnce 4 : list takes more time to execute as compared to tuple.

import timeit

listtime = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]", number=1000000)
tupletime =  timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)", number=1000000)

print("List takes time : ", listtime)
print("Tuple takes time : ", tupletime)



# INSERT, UPDATE AND DELETING TUPLE ELEMENT

# Creating Tuple

# 1. using tuple display construct
tuple1 = ()
tuple2 = ("val1, val2")

# 2. creating empty tuple
tuple1 = tuple()

# 3. Creating single element tuple

tuple1 = (2)    # this will not be a tuple but an integer class
tuple2 = (2,)   #this will be a tuple class.
