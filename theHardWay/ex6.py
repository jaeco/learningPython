#set types_of_people to 10
types_of_people = 10
#set x to a formated string using variable types_of_people
x = f"There are {types_of_people} types of people."

#set binary variable to string
binary = "binary"
#set do_not variable to string
do_not = "don't"
#set y to formated string using variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."
#output the variable x to screen
print(x)
#output the variable y to screen
print(y)
#print formated string using variable x
print(f"I said: {x}")
#print formated string using variable y
print(f"I also said: '{y}'")

#set hilarious boolean to False
hilarious = False
#set joke_evaluation variable to string with an empty argument placeholder
joke_evaluation = "Isn't this joke funny?! {}"
#print to screen result of joke_evaluation using format method, passing in variable hilarious
print(joke_evaluation.format(hilarious))

#set w to string 1
w = "This is the left side of..."
#set e to string 2
e = "a string with a right side."

#string concatination
print(w + e)
