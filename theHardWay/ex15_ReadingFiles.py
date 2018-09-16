#Import argv from sys module
from sys import argv
#taking in a script and filename
script, filename = argv
#open the file from what was passed in
txt = open(filename)

# Don't hard code the file into the script, ask for the filename instead
print(f"Here's your file {filename}:")
#read from the file
print(txt.read())

#Asking for a file as input from the user
print("Type the filename again:")
file_again = input("> ")
#Assigning txt_again to the new file passed in by the user
txt_again = open(file_again)
#same as line 11
print(txt_again.read())
