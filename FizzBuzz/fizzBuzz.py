import sys

while True:
    print('Enter a number')
    response = input()
    try:
        response = int(response)
    except:
        print("Invalid input, please try again. (Whole numbers only)\n")
        continue
    if (response % 3 == 0) & (response % 5 == 0):
        word = "FizzBuzz\n"
    elif response % 3 == 0:
        word = "Fizz\n"
    elif response % 5 == 0:
        word = "Buzz\n"
    else: word = "___"
    print(word)
