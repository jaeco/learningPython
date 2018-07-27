import sys

while True:
    print('Enter a number')
    response = input()
    response = int(response)
    if (response % 3 == 0) & (response % 5 == 0):
        word = "FizzBuzz\n"
    elif response % 3 == 0:
        word = "Fizz\n"
    elif response % 5 == 0:
        word = "Buzz\n"
    else: word = "___"
    print(word)
