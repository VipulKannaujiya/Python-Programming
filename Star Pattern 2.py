n = int(input("Enter the size of pattern: "))
i = 1
while(n>=i):
    j = 1
    while(j <= n):
        print(" *", end="")
        j += 1
    print()
    n -= 1