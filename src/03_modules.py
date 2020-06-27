"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# print out the available functions and parameters for the sys module
print("sys module available functions and params: ")
for x in dir(sys):
    print(x)
# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("command line arguments of sys.argv: ")
for x in sys.argv:
    print("Argument: ", x)
# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS platform I'm using: \n", sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Version of Python I'm Using: \n", sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# print out the available functions and parameters for the os module
print("OS module functions and params: ")
for x in dir(os):
    print(x)
# Print the current process ID
# YOUR CODE HERE
print("Current process ID: \n", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working directory: \n", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("My Machines Login Name: \n", os.getlogin())
