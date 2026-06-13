n = int(input("Enter No. Of Rows : "))
i = 1
while(n > 0):
    b = 1
    while(b < i):
        print(" ", end="")
        b += 1
    j = 1
    while(j <= (n*2)-1):
        print("*", end="")
        j += 1
    n -= 1
    print()
    i += 1