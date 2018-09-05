#nothing special going on here, just a string variable
days = "Mon Tue Wed Thu Fri Sat Sun"
#There are special characters \n being parsed as line returns, so each month starts on a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#print the days
print("Here are the days: ", days)
#print the months, each on a new line
print("Here are the months: ", months)

# Print whatever is between triple double-quotes as written, however special parsing notes are ignored (this is fluffy strings)
print("""
There's something going on here.
With the three double-quotes
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
