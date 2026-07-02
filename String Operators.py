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

