import random
secret_number = random.randint(1, 45)
print("pick a number between 1 to 45")
while True:
    res = input("Guess the number: ")
    if res == secret_number:
        print("Won")
        break
else:
    print("Loose")













