# A dictionary is a cllection which is unordered, changeable and indexed. In Python dictionariesa are written within curly brackets, and they have kaeys and values. Means the dictionary contains two things first is the key and the second is the value.

# create and print dictionary

dict1 = {
    "Brand" : "BMW",
    "Model" : "M3",
    "Price" : 8995500.98,
    "Year" : 2027
}
print(dict1)


# Accessing Items : you can access the items of a dictionary by refering to its key name, inside square brackets.

x = dict1["Brand"]
y = dict1["Model"]
print(x)
print(y)

# there is also a method called .get() for the same task.

z = dict1.get("Price")
print(z)

# Loop through a dictionary.

dict2 = {
    'brand' : 'suzuki',
    'model' : 'dzise',
    'year' : 2000
}

for i in dict2:
    print(i, end=" : ")    # this will print the index values.
    print(dict2[i]) # this will print the values.

# We can use the values() function to return values of dictionary.

for i in dict1.values():
    print(i)

# We can also use items() function to return values of dictionary. 

dict3 = {
    'brand' : 'suzuki',
    'model' : 'dzise',
    'year' : 2000
}
for x,y in dict3.items():
    print(x,y)


# Change values :- you can change the value of a specific item by refering to its key name.

dict3['year'] = 2026
print(dict3)

# Add, Update, Delete Elements of Dictionary
# checking whether a key exists in the dictionary.

dict4 = {
    'brand' : 'suzuki',
    'model' : 'dzise',
    'year' : 2000
}
if 'model' in dict3:
    print("Yes, 'model' is one of the keys in the dictionary")
else:
    print("No, 'model' is not one of the key in the dictionary")

# Adding new element in the dictionary

print(dict1)
dict1['color'] = 'Black'
print(dict1)


# ========================================= Dictionary & its Functions ===============================================

"""
1. len()
2. pop()
3. popitem() - this method removes the last element of the dictionary. But the in the versions before 3.7 it was used to remove the random values.

dict1.popitem()
print(dict1)

4. del() - this keyword removes the item with specified key name.

del dict1['year']
print(dict1)

5. clear()

dict1.clear()
print(dict1)    dict1 = {}.

6. copy()

x = dict1.copy()
print(x)

7. fromkeys() - The fromkeys() method returns a dictionary with the specified keys and the specified value.

x = ('firstkey', 'secondkey', 'thirdkey')
y = 0
dict1 = dict1.fromkeys(x, y)
print(dict1)

8. setdefault() - the setdefault method returns the value of the item with the specified key.
-- if the key does not exist, it inserts the key with the specified value.

Ex : 
    dict1 = {'brand' : 'Suzuki', 'model' : 'Dezire', 'year' : 2000}
    x = dict1.setdefault("brand", "toyota")
    print(x)

9. update() - the update() method inserts the specified items to the dictionary.

dict1 = {'brand' : 'Suzuki', 'model' : 'Dezire', 'year' : 2000}
dict1.update("color", "white")
print(dict1)
"""