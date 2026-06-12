age = int(input("Enter your age: "))
x = 'You are eligible for voting' if age > 18 else 'You are not eligible for voting'
print(x)

x = 'You are young' if (age > 18 and age < 40) else 'You are child'
print(x)
