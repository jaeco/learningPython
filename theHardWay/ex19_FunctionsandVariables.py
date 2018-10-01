# Define cheese_and_crackers function passing in two args of cheese_count and boxes_of_crackers
# def cheese_and_crackers(cheese_count, boxes_of_crackers):
# lots of print statements
    # print(f"You have {cheese_count} cheeses!")
    # print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print(f"Man that's enough for a party!")
    # print("Get a blanket.\n")

# print("We can just give the function numbers directly:")
# cheese_and_crackers(20, 30) #passing in hardcode numbers of 20 and 30

# print("OR, we can use variables from our script:")
# amount_of_cheese = 10
# amount_of_crackers = 50
# #Calling the function cheese_and_crackers this time passing in variables set beforehand
# cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print("We can even do math inside too:")
# cheese_and_crackers(10 + 20, 5 + 6) # Now we're passing in numbers but performing math first

# print("And we can combine the two, variables and math:")
# cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Variables and math!

##############
## Write your own function and call it 10 different ways
##############

def jelly_and_sandwiches(jelly_jars, bread_slices):
# Lets make sure we have an even amount of bread slices to ensure a sandwich
    if bread_slices % 2 == 0:
        print(f"You have {jelly_jars} jars of jelly and {bread_slices} slices of bread!")
    else:
        print(f"Sorry, you have an uneven amount of bread_slices ({bread_slices}), we don't make half sandwiches here.")

# jars = 8
# slices = 20

# Call 1
# jelly_and_sandwiches(2, 10)

# Call 2
# jelly_and_sandwiches(jars, slices)

# Call 3
# jelly_and_sandwiches(jars + 5, slices + 2)

# Call 4
# print("How many jars and slices do you want to use? (Jars first then slices):")
# jelly_and_sandwiches(int(input()), int(input()))

# Call 5
# jelly_and_sandwiches(8 + 2, 6 + 14)

# Call 6
# def how_many_jars():
    # print("How many jars?")

# def how_many_slices():
    # print("How many slices?")

# jelly_and_sandwiches(int(input(how_many_jars())), int(input(how_many_slices())))

# Call 7
# def how_many_jars(jars):
#     return jars
# def how_many_slices(slices):
#     return slices

# jelly_and_sandwiches(how_many_jars(2), how_many_slices(6))

# Call 8
from sys import argv
def jars_and_slices(jars, slices):
    jelly = int(jars)
    bread = int(slices)
    print(f"You have {jelly} jelly and {bread} bread")
    jelly_and_sandwiches(jelly, bread)
jars_and_slices(jars, slices)

# Call 9


# Call 10
