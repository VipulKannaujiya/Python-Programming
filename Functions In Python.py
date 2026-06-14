# Function Without parameter, without reutrn

#Function Declaration
def say_hello():
    print("Namaste, Python!")

# Function Call
say_hello()

print("===========================================================================")

# Function With Parameter(Input)
def greet(name):
    print("Namaste,", name)

name = input("Enter Your Name: ")
greet(name)

print("===========================================================================")

# Function With Return(Output)
def sum(a, b):
    result = a + b
    return result

n1 = int(input("Enter First No. : "))
n2 = int(input("Enter Second No. : "))
print("Sum = ", sum(n1,n2))

print("===========================================================================")

# Multiple value return karna
def cal(a, b):
    sum = a + b
    sub = a - b
    return sum, sub

# n1 = int(input("Enter First No. : "))
# n2 = int(input("Enter Second No. : "))
x, y = cal(23, 7)
print("Sum = ", x)
print("Sub = ", y)

print("===========================================================================")

# Positional Parameter(normal)
# jo order me pass karte ho, usi order me assign hote hain.
def power(base, exp):
    return base ** exp

print("2 ** 3 = ",power(2, 3))

print("===========================================================================")

# Default Parameter
# Agar argument na do, to default value use ho jayegi.
def greet(name="Guest"):
    print("Hello", name)

greet("vipul")
greet()

print("===========================================================================")

# Keyword Arguments
def intro(name, age):
    print("Name : ", name, "Age : ", age)

intro(name = "Vipul ", age = 20)
