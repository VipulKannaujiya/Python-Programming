def add(a, b):
    print("\n",a, "+", b, "=", a + b)

def subtract(a, b):
    print("\n",a, "-", b, "=", a - b)

def multiply(a, b):
    print("\n",a, "*", b, "=", a * b)

def divide(a, b):
    if b != 0:
        print("\n",a, "/", b, "=", a / b)
    else:
        print("Error: Division by zero is not allowed.")
def remainder(a, b):
    if b != 0:
        print("\n",a, "%", b, "=", a % b)
    else:
        print("Error: Division by zero is not allowed.")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Exit")

    choice = input("\nEnter choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Exiting the calculator.")
        break

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        add(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiply(num1, num2)
    elif choice == '4':
        divide(num1, num2)
    elif choice == '5':
        remainder(num1, num2)
    else:
        print("Invalid input. Please try again.")

    ch = input("\nDo you want to perform another calculation? (yes/no): ")
    if ch.lower() != 'yes':
        print("Exiting the calculator.")
        break