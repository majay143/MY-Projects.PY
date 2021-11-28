val = input("Enter your value: ")
print(val)
num = input("Enter number: ")
print(num)
name1 = input("Enter your name: ")
print(name1)

# printing type of input value
print("type of number", type(num))
print("type of name", type(name1))

# Using list comprehension taking multiple values
# taking two input values at a time
x, y = [int(x) for x in input("Enter two value: ").split()]
print("First number is: ", x)
print("Second number is: ", y)
print()

# taking two inputs at a time
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First number is {} and second number is {}".format(x, y))

# taking multiple values at a time
x, y = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x)
# FizzBuzz program
for fizzbuzz in range(100):
    if fizzbuzz % 2 == 0:
        print("FIZZBUZZ")
        continue
    elif fizzbuzz % 5 == 0:
        print("FIZZ")
        continue
    elif fizzbuzz % 3 == 0:
        print("BUZZ")
        continue
    else:
        print("X")






