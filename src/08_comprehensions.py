"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
y = []
# this will edit the list y:
# for x in range(5):
#     y.append(x+1)
# print (y)
# this will not edit the list y, rather it will write a list comprehension to produce another array:
list_comprehension = list(map(lambda x: x + 1, range(5)))
# or similarly
list_comprehension2 = [x + 1 for x in range(5)]
print("list of 1-5 with map and lambda list comprehension", list_comprehension)
print("list of 1-5 with for loop", list_comprehension2)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
list_comp_cubed = list(map(lambda x: x**3, range(10)))
print(list_comp_cubed)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
y = list(map(lambda x: x.upper(), a))
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
newx = list(map(lambda x: int(x), x))
print("old x", x)
print("new x", newx)

# What do you need between the square brackets to make it work? I need to change strings to ints first.
y = [num for num in newx if num % 2 == 0]

print(y)