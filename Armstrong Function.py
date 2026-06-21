def is_armstrong(n):
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem ** 3
        n = n // 10
    return sum

n = int(input("Enter Any Number : "))
temp = n
if(temp == is_armstrong(n)):
    print("Your Number Is Armstrong Number....")
else:
    print("Your Number Is Not Armstrong Number....")