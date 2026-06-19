def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime Number...")
            return
    
    print("Prime Number...")

n = int(input("Enter Any Number: "))
is_prime(n)