import random


print("Hello to the Number Guessing Game")

print("please enter the range between the numbers you want")
value = int(input("please enter the first range:"))
value2 = int(input("please enter the second range:"))
value3 = int(input("please enter the number between the range:"))
r = random.randrange(value, value2)

while value <= value3 <= value2 and value3 != r:
    if value3 < r:
        print("the answer is lower than the random number")
        value3 = int(input("please enter the number again:"))
    elif value3 > r:
        print("the number is higher than random number")
        value3 = int(input("please enter the number again:"))
    else:
        break
print("correct!")

    


