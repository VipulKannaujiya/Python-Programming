def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

string = input("Enter Any String Value : ")
print(" ", reverse_string(string))