# 1. max() - This method is used to find max value present in the list.

a = [10, 20, 30, 40, 50]
print("Max value in the list = ", max(a))

# 2. min() - This method is used to find min value present in the list.

a = [10, 20, 30, 40, 50]
print("Min value in the list = ", min(a))

# 3. cmp(list1, list2) - This method is used to compare two list.
# cmp() function python 2 ka hissa tha jo ki ab ke versions me nahi hai.
# Yeh function bilkul purane cmp() jaisa hi kaam karega
def cmp(l1, l2):
    if l1 == l2:
        return 0
    elif l1 < l2:
        return -1
    else:
        return 1

list1 = [2,4,6,8]
list2 = [2,4,6,8]
list3 = [2,4,6,9,11]
list4 = [2,4,6,8]
print("Comparing list1 and list2 : ")
print(cmp(list1,list2))
print("Comparing list2 and list3 : ")
print(cmp(list2,list3))
print("Comparing list1 and list4 : ")
print(cmp(list1,list4))

# 4. append() - This method is used to append(add) a passed object at the end of the list, Note that the object is added to the last of the list.

name = ["Ram", "shyam", "sita", "gita"]
print(name)
name.append("rita")
print(name)

# 5. count() - This method is uset to count the frequency of a given object.

name = ["Ram", "shyam", "sita", "gita", "Ram","Ram", "sita"]
freq = name.count("Ram")
print(freq)
freq = name.count("sita")
print(freq)

# 6. index() - This method is used to find the index of the object/element. This function returns the first index of the object/index if it is found otherwise it returns an exceptions showing that the element is not found.

name = ["Ram", "shyam", "sita", "gita"]
ind = name.index("Ram")
print(ind)

# 7. insert(index,object) - This method is used to insert an object/value at the given index.

a = [5, "Vipul", 10]
print(a)
a.insert(2, "Hi")
print(a)

# 8. remove(object) - This method is used to delete an object/value from the given list. Note that it removes/deletes the first occurrence of the list.

a = ["ram", 5, 10, "ravi", 10]
print(a)
a.remove(10)
print(a)

# 9. reverse() - This method is used to reverse the element presents in the list in place. Here the word, in place means that the list gets reversed itself.

a = ["l", "u", "p", "i", "V"]
print(a)
a.reverse()
print(a)

# 10. sort() - This method is used to sort the elements present in the list in either ascending order or in descending order.

a = [1,44,53,6,3,8,4,6,29,34,74,33]
print(a)
a.sort()
print(a)

# 11. pop() - This method is used to delete the last element from the list. Note that this fuction deletes the last element from the list one by one.

a = [1,44,53,6,3,8,4,6,29,34,74,33]
print(a)
a.pop()
print(a)