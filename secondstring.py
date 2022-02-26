# Explanation: a program to reverse a string and print out each alternating character.

# Task: Write a program that asks a user to input a string and outputs every second letter in reverse order.

# Solution sources were [W3Schools' pages on how to reverse strings and the slice function. Both links are
# in the README file.]

# Working notes: I couldn't get the [::-1] syntax that W3 was giving me to work without also defining a 
# function, so I've determined the start point of the function by calculating the length of the string as 
# inputLen and setting the end point as zero. I also initially set this as 1 but it then skipped the final
# character.

userInput = input ( "Please enter a sentence: " )
inputLen = len ( userInput )
slicer = slice ( inputLen , 0 , -2 )

print ( userInput [ slicer ] )