# -*- coding: utf-8 -*- 
# This is my first Python document. I'm proud of it :)

print("Hello world!")

# This is a comment, so I can read and understand what my program does if I come back to it at a later date.
# Remember that anything that comes after the # is ignored by Python.

print("I could have code like this.") # and the comment after is ignored.

# You can also use a comment to "disable" or "comment out" a piece of code.

# print("This will NOT run.")

print("This will run.")

print("From this point on I'll be using more than just the print command and comments. It's time to do math!")

print("I will now count chickens.")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs.")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print (3 + 2 < 5 - 7)

print("What is 3 + 2?")
print("What is 5 - 7?")

print("Oh, that's why it's False.")

print("How about some more?")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Now it is time to do some more interesting things. I will create my own variables to use in math equations.

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "people to carpool today.")
print("We need to put about", average_passengers_per_car, "people in each car.")

# It's time to do more variables, now even more advanced than last time.

my_name = 'Nebby Sarak'
my_age = 25 # not a lie or anything
my_height = 70 # inches, hypothetical
my_weight = 91 # lbs
my_eyes = 'Green'
my_teeth = 'Yellowish'
my_hair = 'Blonde'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually he's not too heavy at all.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair) )
print("His teeth are usually %s depending on when he decides to brush them." % my_teeth)

# this line is tricky, but I'll try to get it exactly right

print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight) )