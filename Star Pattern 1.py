n = int(input("Enter the size of pattern: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(" *", end="")
        j += 1
    print()
    i += 1
print()
print("Star Pattern 1 Printed Successfully.....")