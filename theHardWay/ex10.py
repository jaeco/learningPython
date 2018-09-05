# the \t escape sequence will tab in the following line
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line." # put the text after the \n on a new line
backslash_cat = "I'm \\ a \\ cat." # escape a backslash for each \\

# Write out what is written as it is written, with escape sequence parsing
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
