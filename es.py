# Explanation: a program that counts the number of times a given character occurs in a given .txt file.

# Task: Write a program that reads in a text file and outputs the number of e's it contains. Think 
# about what is being asked here, document any assumptions you are making. The program should take 
# the filename from an argument on the command line. I have not shown you how to do this, you need 
# to look it up.

# Sources were

# Working Notes: The first part of the solution was bringing in the file name as part of the command,
# rather than using a user input or hard-coding the filename into the sources. I found a simple solution
# using the sys.argv command that allowed this, then I just had a to set up a one-line .txt file to test
# it.

import sys

with open(sys.argv[1],"r") as f:
    contents = f.read()
print (contents)
