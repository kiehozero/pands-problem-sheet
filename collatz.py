# Explanation: 

# Task: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate 
# the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if 
# the current value is one. 

# Please enter a positive integer: 10

# 10 5 16 8 4 2 1

# Solution sources: the lecture notes were largely sufficient to complete this, this was more of a challenge in actually working out how to convert my brain's 
# logic into working Python. I had to Google how to print individual items as a list, the answer of which was ridiculously simple thanks to DataScienceParichay

# Working notes: first problem I encountered as usual was not ensuring that entries were integers. I then had a couple of phases of moving the append and the next
# input in and out of various parts of the loop. I also misunderstood the original request that the user should input the new number at each stage rather than
# calculating everything from an initial submission. After getting a horrific infinite loop on the second try (see commit history), I realised that I needed to
# define the output as the next input, as well as adding the original user submission to the list, so I swapped the first two lines of code around and removed the
# final lines of code that repeated the number 1 being appended.

numerator = int ( input ( "Please enter a positive number: ") )

enteredNums = [numerator]

while numerator != 1 :
    if ( numerator % 2 ) == 0 :
        result = int ( ( numerator / 2 ) )
        enteredNums.append ( result )
        print ( enteredNums )
        numerator = result
    else:
        result = int ( ( numerator * 3 ) + 1 )
        enteredNums.append ( result )
        print ( enteredNums )
        numerator = result