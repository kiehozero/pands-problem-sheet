# Explanation: a program that counts the number of times a given character occurs in a given .txt file.

# Task: Write a program that reads in a text file and outputs the number of e's it contains. Think 
# about what is being asked here, document any assumptions you are making. The program should take 
# the filename from an argument on the command line. I have not shown you how to do this, you need 
# to look it up.

# Sources were a StackOverflow thread that for the command line entry, while the count() method came 
# from GeeksForGeeks. I tested this program on a Moby Dick txt file that a GitHub user called Steven 
# Klontz uploaded. All links are in the README.

# Working Notes: The first part of the solution was bringing in the file name as part of the command,
# rather than using a user input or hard-coding the filename into the sources. I found a simple solution
# using the sys.argv command that allowed this, then I just had a to set up a one-line .txt file to test
# it. 

# The GeeksForGeeks article above highlighted three methods for counting characters; I used what I 
# considered to be the cleanest method of the three. The first method was a 'for' loop, while the third
# method required importing a function that achieved the same result as the second method, which is a 
# built-in function, and so seemed the most obvious to use.

# An error that I noticed was when I was testing on the Moby Dick txt file. After running another file, 
# i realised that my program was case-sensitive. Adding the lower() function was enough to get this 
# counting correctly, by storing a lower-case-only version of the file as a separate variable.

import sys

with open ( sys.argv [ 1 ] , "r" ) as f:
    contents = f.read ( )
    noCaps = contents.lower ( )
    counter = noCaps.count ('e')
print ( counter )
