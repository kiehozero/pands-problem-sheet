# Explanation: 

# Task: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate 
# the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if 
# the current value is one. 

# Please enter a positive integer: 10

# 10 5 16 8 4 2 1

# Solution sources: 

# Working notes: first problem I encountered as usual was not ensuring that entries were integers. I then had a couple of phases of moving the append and the next
# input in and out of various parts of the loop. I also misunderstood the original request that the user should input the new number at each stage rather than
# calculating everything from an initial submission.

enteredNums = []

numerator = int ( input ( "Please enter a positive number: ") )

while numerator != 1 :
    if ( numerator % 2 ) == 0 :
        result = int ( ( userNum / 2 ) )
        enteredNums.append ( result )
        print ( enteredNums )
        numerator = int ( input ( "Please enter a positive number: ") )
    result = int ( ( userNum * 3 ) + 1 )
    enteredNums.append ( result )
    print ( enteredNums )
    userNum = int ( input ( "Please enter a positive number: ") )