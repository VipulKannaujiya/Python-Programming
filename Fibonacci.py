def fibonacci(n):
    a = 0
    b = 1
    print()
    for i in range(n):
        print(" ", a, end="")
        c = a + b
        a = b
        b = c

n = int(input("Enter Any Number : "))
fibonacci(n)