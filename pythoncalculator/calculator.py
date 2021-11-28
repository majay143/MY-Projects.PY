# calculator in  python


print("Select an operation to perform:")
print("1. ADD")   # priority of operators
print("2. SUB")
print("3. MUL")
print("4. DIV")
operation = input()
if operation == "1":
    num1 = input("Enter num1")
    num2 = input("Enter num2")
    print("Sum is " + str(int(num1)+int(num2)))
elif operation == "2":
    num1 = input("Enter num1")
    num2 = input("Enter num2")
    print("DIFF is " + num1 - num2)
elif operation == "3":
    num1 = input("Enter num1")
    num2 = input("Enter num2")
    print("DIFF is " + num1 * num2)
elif operation == "4":
    num1 = input("Enter num1")
    num2 = input("Enter num2")
    print("DIFF is " + num1 / num2)

else:
    print("Invalid Entry")


