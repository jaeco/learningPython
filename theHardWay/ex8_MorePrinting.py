# Set variable formatter to a string that takes in 4 seperate arguments
#  ITS LIKE AN ARRAY OF SORTS!...sort of?
formatter = "{} {} {} {}"

# print out a line with the variable formatter, using the format argument to pass in 4 arguments of various types
print(formatter.format(1, 2, 3, 4, 5)) #Extra arguments get ignored
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True)) #these are keywords, Python recognizes that
print(formatter.format(formatter, formatter, formatter, formatter)) #Why not just pass in the string itself?
# White space? What white space?
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
