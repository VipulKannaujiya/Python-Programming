def fact(n):
    f = 1
    while(n > 0):
        f = f * n
        n -= 1
    return f

a = int(input("Enter Any Number : "))
print("Factorial Of Given Number Is ", fact(a))