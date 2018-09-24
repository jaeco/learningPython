#Script to read the file we just wrote in ex16
from sys import argv
script, filename = argv

txt = open(filename)

print(f"Opening file -- {filename}:\n--------SOF----------\n")
print(txt.read())
print(f"--------EOF----------\nClosing file -- {filename}")

txt.close()
