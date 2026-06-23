# WAF jo check kare ki string palindrom hai ya nahi.

def is_palindrom(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

string = input("Enter Any String Value : ")
temp = string
if(temp == is_palindrom(string)):
    print("Your Character Is Palindrom.")
else:
    print("Your Character is not Palindrom.")