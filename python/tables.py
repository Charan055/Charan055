print('\nA program to print a table...!\n')
table = int(input("What table do you want me to print : "))
print("\n")
print("-----------\n")
for i in range(10):
    print(table, '*', (i+1), "=", table*(i+1))
print("\n---The End---\n")
