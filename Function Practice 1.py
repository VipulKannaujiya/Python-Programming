# Q1 - Ek function 'say_hello()' banao jo screen par 'Hello World' print kare.

def say_hello():
    print("Hello World")
say_hello()

# Q2 - Ek function 'greet(name)' banao jo screen par 'Hello, <name>' print kare.

def greet(name):
    print("Hello,", name)
name = input("Enter Your Name : ")
greet(name)

# Q3 - Ek function 'add_two_numbers()' banao jo user se 2 number input le aur uska sum print kare.

def add_two_numbers(a, b):
    sum = a + b
    print(a ,"+", b ,"=", sum)

x = int(input("Enter First Number : "))
y = int(input("Enter Second Number : "))
add_two_numbers(x, y)

# Q4 - Ek function 'even_or_odd(n)' banao jo bataye ki number even hai ya odd.

def even_or_odd(n):
    if(n % 2 == 0):
        print(n, "Is Even Number.")
    else:
        print(n, "Is Odd Number.")
n = int(input("Enter Any Number To Check Even Or Odd : "))
even_or_odd(n)

# Q5 - Ek function 'max_of_two(a,b)' banao jo do number me se bada number return kare.

def max_of_two(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print("Both Are Equal....")

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
max = max_of_two(a, b)
print(max, "Is Max Number;")