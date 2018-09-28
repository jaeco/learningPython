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

jars = 8
slices = 20

#1
jelly_and_sandwiches(2, 10)

#2
jelly_and_sandwiches(jars, slices)

#3
jelly_and_sandwiches(jars + 5, slices + 2)

#4
print("How many jars and slices do you want to use? (Jars first then slices):")
jelly_and_sandwiches(int(input()), int(input()))

#5


#6


#7


#8


#9


#10
