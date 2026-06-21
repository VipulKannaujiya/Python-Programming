def is_perfect(n):
    sum = 0
    i = 1
    while(i < n):
        if(n % i == 0):
            sum = sum + i
        i += 1
    return sum

n = int(input("Enter any number : "))
temp = n

if(temp == is_perfect(n)):
    print("Perfect Number")
else:
    print("Not Perfect Number")