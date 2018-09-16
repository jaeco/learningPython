from sys import argv

script, filename = argv

txt = open(filename)

# Don't hard code the file into the script, ask for the filename instead
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
