# 1. Concatenation Operator (+)
# The concatenation operator (+) is used to combine two or more strings into a single string

string1 = "Vipul "
string2 = "Kannaujiya"
string3 = string1 + string2
print(string3)


# 2. Repetition Operator (*)
# The repetition operator (*) is used to repeat a string a specified number of times

string4 = "Vipul "
string5 = string4 * 3
print(string5)


# 3. Membership Operator (in/not in)
# The membership operator (in) is used to check if a string is present in another string.
# The membership operator (not in) is used to check if a string is not present in another string.

string6 = "Vipul Kannaujiya"
string7 = "Vipul"

print(string7 in string6)  # True
print(string7 not in string6)  # False

# 4. Comparison Operators (==, !=, <, >, <=, >=)
# The comparison operators are used to compare two strings and return a boolean value (True or False).

string8 = "Vipul"
string9 = "Kannaujiya"
string10 = "Vipul"

print(string8 == string9)  # False
print(string8 == string10)  # True
print(string8 != string9)  # True
print(string8 < string9)  # True
print(string8 > string9)  # False
print(string8 <= string9)  # True
print(string8 >= string9)  # False

# 5. String Formatting Operator (%)
# The string formatting operator (%) is used to format strings by replacing placeholders with values.
name = "Vipul"
age = 25
print("My name is %s and I am %d years old." % (name, age))

# ----------------------------------------------- PRE - DEFINED FUNCTION -------------------------------------------------
# Built-in functions ki list khud kaise dekh sakte hai python me, bas aapko ye command run karna hoga
import builtins
print(dir(builtins))

#-------------------------------------------Number / Math related  built-ins----------------------------------------------

# 1. abs() - Returns the absolute value of a number
print()
print(abs(-5))  # 5

# 2. round() - Rounds a number to the nearest integer or to a specified number of decimal places
print("3.14159 -> ",round(3.14159, 2))  # 3.14

# 3. pow() - Returns the value of a number raised to the power of another number
print(pow(2, 3))  # 8

# 4. divmod() - Returns a tuple containing the quotient and remainder of a division operation
print(divmod(10, 3))  # (3, 1) -- 10 % 3 = 1, 10 // 3 = 3.

# 5. sum() - Returns the sum of all items in an iterable (e.g., list, tuple)
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 15

# 6. max() - Returns the largest item in an iterable or the largest of two or more arguments.
print(max(numbers))  # 5

# 7. min() - Returns the smallest item in an iterable or the smallest of two or more arguments.
print(min(numbers))  # 1

#----------------------------------------- Boolean / iterable check -----------------------------------------------

# 8. all() - Returns True if all items in an iterable are true (or if the iterable is empty).
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False

# 9. any() - Returns True if any item in an iterable is true. If the iterable is empty, returns False.
print(any([False, False, True]))  # True
print(any([False, False, False]))  # False

#----------------------------------------- Type Conversion / constructors -----------------------------------------------

# 10. bool() - Converts a value to a Boolean (True or False).
print(bool(1))  # True
print(bool(0))  # False

# 11. int() - Converts a value to an integer.
print(int(3.14))  # 3
print(int("123"))  # 123

# 12. float() - Converts a value to a floating-point number.
print(float(3))  # 3.0
print(float("3.14"))  # 3.14

# 13. complex() - Converts a value to a complex number.
print(complex(3, 4))  # (3+4j)

# 14. str() - Converts a value to a string.
print(str(123))  # '123'

# 15. list() - Converts an iterable (e.g., string, tuple) to a list.
print(list("Vipul"))  # ['V', 'i', 'p', 'u', 'l']

# 16. tuple() - Converts an iterable (e.g., string, list) to a tuple.
print(tuple("Vipul"))  # ('V', 'i', 'p', 'u', 'l')

# 17. dict() - Converts a sequence of key-value pairs (e.g., list of tuples) to a dictionary.
pairs = [("a", 1), ("b", 2), ("c", 3)]
print(dict(pairs))  # {'a': 1, 'b': 2, 'c': 3}

# 18. set() - Converts an iterable (e.g., list, string) to a set (removes duplicates).
print(set([1, 2, 2, 3, 4, 4, 5]))  # {1, 2, 3, 4, 5}

# 19. frozenset() - Converts an iterable to a frozenset (an immutable set).
print(frozenset([1, 2, 2, 3, 4, 4, 5]))  # frozenset({1, 2, 3, 4, 5})

# 20. bytes() - Converts a string or iterable of integers to a bytes object.
print(bytes("Vipul", "utf-8"))  # b'Vipul'

# 21. bytearray() - Converts a string or iterable of integers to a bytearray object.
print(bytearray("Vipul", "utf-8"))  # bytearray(b'Vipul')

# 22. memoryview() - Returns a memory view object of a bytes-like object.
print(memoryview(b"Vipul"))  # <memory at 0x7f8e8c0b0>

# 23. range() - Returns a range object that represents a sequence of numbers.
print(list(range(5)))  # [0, 1, 2, 3, 4]

# 24. slice() - Returns a slice object that can be used to slice sequences (e.g., lists, strings).
my_list = [0, 1, 2, 3, 4, 5]
my_slice = slice(1, 4)
print(my_list[my_slice])  # [1, 2, 3]

# 25. object() - Returns a new featureless object. It is a base for all classes.
obj = object()
print(obj)  # <object object at 0x7f8e8c0b0>

#----------------------------------------- Iterator / Fuctional tools -----------------------------------------------

# 26. iter() - Returns an iterator object for an iterable (e.g., list, tuple).
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# 27. next() - Returns the next item from an iterator. If the iterator is exhausted, it raises StopIteration.
my_iterator = iter(my_list)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3

# 28. aiter() - Returns an asynchronous iterator object for an asynchronous iterable (e.g., async generator).
# Note: This function is available in Python 3.10 and later.

# 29. anext() - Returns the next item from an asynchronous iterator. If the iterator is exhausted, it raises StopAsyncIteration.
# Note: This function is available in Python 3.10 and later.

# 30. enumerate() - Returns an enumerate object that yields pairs of index and value from an iterable.
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(index, value)  # 0 'a', 1 'b', 2 'c'

# 31. filter() - Returns an iterator that filters elements from an iterable based on a function.
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # [2, 4, 6]

# 32. map() - Returns an iterator that applies a function to every item of an iterable.
def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25]

# 33. zip() - Returns an iterator that aggregates elements from multiple iterables.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]

# 34. reversed() - Returns a reverse iterator for a sequence (e.g., list, string).
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # [5, 4, 3, 2, 1]

# 35. sorted() - Returns a new sorted list from the items in an iterable.
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 5, 6, 9]

# ------------------------------------------ Input / Output / Debugging -----------------------------------------------

# 36. print() - Prints the specified message to the console or other standard output device.
print("Hello, World!")  # Hello, World!

# 37. input() - Reads a line of text from the user and returns it as a string.
# user_input = input("Enter something: ")

# 38. open() - Opens a file and returns a file object. It can be used to read or write files.
# file = open("example.txt", "r")

# 39. help() - Invokes the built-in help system. It can be used to get information about modules, classes, functions, etc.
help(print)  # Displays help information for the print function

# 40. dir() - Returns a list of the attributes and methods of an object. It can be used to inspect objects.
print(dir(str))  # Displays the attributes and methods of the str class

# 41. breakpoint() - Enters the debugger at the call site. It can be used to set breakpoints in the code for debugging.
# breakpoint()  # Uncomment this line to enter the debugger

# ------------------------------------------ Representation / encoding / decoding -----------------------------------------------

# 42. repr() - Returns a string representation of an object that can be used to recreate the object.
my_list = [1, 2, 3]
print(repr(my_list))  # [1, 2, 3]

# 43. ascii() - Returns a string containing a printable representation of an object, escaping non-ASCII characters.
my_string = "Hello, 世界"
print(ascii(my_string))  # 'Hello, \u4e16\u754c'

# 44. format() - Returns a formatted string using placeholders and values.
name = "Vipul"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # My name is Vipul and I am 25 years old.

# 45. bin(), oct(), hex() - Convert an integer to a binary, octal, or hexadecimal string representation.
number = 42
print(bin(number))  # 0b101010
print(oct(number))  # 0o52
print(hex(number))  # 0x2a

# 46. ord() - Returns the Unicode code point of a character.
print(ord('A'))  # 65

# 47. chr() - Returns the character corresponding to a Unicode code point.
print(chr(65))  # 'A'

# 48. hash() - Returns the hash value of an object (if it has one). It can be used to compare objects and store them in hash-based data structures (e.g., sets, dictionaries).
print(hash("Vipul"))  # Hash value of the string "Vipul"

# ------------------------------------------ Object / Classes / attributes -----------------------------------------------

# 49. type() - Returns the type of an object. It can be used to check the type of variables and objects.
print(type(42))  # <class 'int'>

# 50. isinstance() - Checks if an object is an instance of a specified class or a subclass thereof.
print(isinstance(42, int))  # True

# 51. issubclass() - Checks if a class is a subclass of another class.
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True

# 52. id() - Returns the unique identifier of an object. It can be used to check if two variables refer to the same object in memory.
x = [1, 2, 3]
y = x
print(id(x))  # Unique identifier of the list object
print(id(y))  # Same unique identifier as x

# 53. callable() - Checks if an object appears callable (i.e., can be called as a function).
def my_function():
    pass

print(callable(my_function))  # True

# 54. getattr() - Returns the value of a named attribute of an object. It can be used to access attributes dynamically.
class MyClass:
    def __init__(self):
        self.attribute = "Hello"

obj = MyClass()
print(getattr(obj, "attribute"))  # "Hello"

# 55. setattr() - Sets the value of a named attribute of an object. It can be used to modify attributes dynamically.
setattr(obj, "attribute", "World")
print(getattr(obj, "attribute"))  # "World"

# 56. delattr() - Deletes a named attribute of an object. It can be used to remove attributes dynamically.
delattr(obj, "attribute")
print(getattr(obj, "attribute"))  # AttributeError: 'MyClass' object has no attribute 'attribute'

# 57. hasattr() - Checks if an object has a named attribute. It can be used to check for the existence of attributes dynamically.
print(hasattr(obj, "attribute"))  # False

# 58. vars() - Returns the __dict__ attribute of an object, which is a dictionary containing the object's writable attributes.
class MyClass:
    def __init__(self):
        self.attribute1 = "Hello"
        self.attribute2 = "World"

obj = MyClass()
print(vars(obj))  # {'attribute1': 'Hello', 'attribute2': 'World'}

# 59. locals() - Returns a dictionary containing the current local symbol table. It can be used to inspect local variables.
def my_function():
    local_variable = "Hello"
    print(locals())  # {'local_variable': 'Hello'}

# 60. globals() - Returns a dictionary containing the current global symbol table. It can be used to inspect global variables.
global_variable = "Hello"
print(globals())  # {'global_variable': 'Hello'}

# 61. super() - Returns a proxy object that delegates method calls to a parent or sibling class. It can be used to call methods from a superclass.
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls Parent.greet()
        print("Hello from Child")

child = Child()
child.greet()

# 62. property() - Returns a property attribute for a class. It can be used to define getter, setter, and deleter methods for an attribute.
class MyClass:
    def __init__(self):
        self._attribute = "Hello"

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        self._attribute = value

obj = MyClass()
print(obj.attribute)  # "Hello"
obj.attribute = "World"
print(obj.attribute)  # "World"

# 63. classmethod() - Returns a class method for a class. It can be used to define methods that operate on the class itself rather than instances of the class.
class MyClass:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        print(cls.class_variable)
    
MyClass.class_method()  # "Hello"

# 64. staticmethod() - Returns a static method for a class. It can be used to define methods that do not operate on instances or the class itself.
class MyClass:
    @staticmethod
    def static_method():
        print("Hello from static method")
    
MyClass.static_method()  # "Hello from static method"


# ------------------------------------------- Code Execution / import -----------------------------------------------