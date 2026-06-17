def simple_Interest(p,r,t):
    si = p * r * t // 100
    return si

a = int(input("Enter Principle Amount : "))
b = int(input("Enter Rate Of Interest(%) : "))
c = int(input("Enter Time Of Interest(In Year) : "))
print()
print("Total Simple Interest is : ", simple_Interest(a, b, c))