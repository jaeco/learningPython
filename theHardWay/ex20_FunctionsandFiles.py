#Importing the argv module from sys
from sys import argv

script, input_file = argv #Capturing passed in arguments after the script runs

def print_all(f): #Function to print everything from the object is passed in
    print(f.read())

def rewind(f): #Move to the first position of the object passed in
    f.seek(0)

def print_a_line(line_count, f): #Print out the line count passed in, read the first (or next) line of the object passed in
    print(f"Printing line: {line_count}")
    print(f.readline())

current_file = open(input_file) #open the file passed into the script

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
