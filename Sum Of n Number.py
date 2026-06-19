def sum_of_n(n):
    sum = 0
    for i in range(0, n+1):
        sum = sum + i
    return sum

n = int(input("Enter A Number : "))
print("Sum Of Your Given Number = ", sum_of_n(n))