"""
n = int(input("Enter no. for printing table: "))
i = 1
while(i<=10):
    table = n*i
    print(table)
    i += 1
"""
choice = 'yes'
while(choice == 'yes'):
    if choice == 'yes':
        n = int(input("Enter no. for printing table: "))
        i = 1
        while(i<=10):
            table = n*i
            print(table)
            i += 1
        choice = (input("Do you want print again (yes/no): "))

else:
    print("Your table is printed successfully!!!!!")

