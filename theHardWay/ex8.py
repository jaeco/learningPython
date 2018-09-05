# Set variable formatter to a string that takes in 4 seperate arguments
#  ITS LIKE AN ARRAY OF SORTS!...sort of?
formatter = "{} {} {} {}"

# print out a line with the variable formatter, using the format argument to pass in 4 numbers per argument
print(formatter.format(1, 2, 3, 4, 5)) #Extra arguments get ignored
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
