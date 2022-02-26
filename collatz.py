# Explanation: A program to simply demonstrate the Collatz conjecture.

# Task: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate 
# the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if 
# the current value is one. 

# Please enter a positive integer: 10

# 10 5 16 8 4 2 1

# Sources: the lecture notes were largely sufficient to complete this, this was more of a challenge in actually working out how to convert my brain's 
# logic into working Python. I had to Google how to print individual items as a list, the answer of which was ridiculously simple thanks to DataScienceParichay,
# and I also somehow needed a reminder of using the append method for lists, which is credited to W3 schools in the README.

# Working notes: The first problem I encountered as usual was not ensuring that entries were integers. I then had a couple of phases of moving the append and 
# the next input in and out of various parts of the loop. I also misunderstood the original request that the user should input the new number at each stage 
# rather than calculating everything from an initial submission. After getting a horrific infinite loop on the second try (see commit history), I realised that 
# I needed to define the output as the next input, as well as adding the original user submission to the list, so I swapped the first two lines of code around 
# and removed the final lines of code that repeated the number 1 being appended. After Googling for a solution to printing the items of a list separately but on 
# the same line instead of all within square brackets, I used the asterisk as outlined in the DataScienceParichay link (heading 'Using * operator to unpack the 
# list') in the README.

numerator = int ( input ( "Please enter a positive number: ") )

# pushes the initial numerator value to the list
enteredNums = [ numerator ]

while numerator != 1 :
    # divides any even numbers by 2 and adds them to the list
    if ( numerator % 2 ) == 0 :
        result = int ( ( numerator / 2 ) )
        enteredNums.append ( result )
        # establishes the result of this operation as the numerator of the next at line 28
        numerator = result
    else:
        # multiples any odd numbers by 3 and adds 1, thus re-establishing an even number as the numerator at line 28
        result = int ( ( numerator * 3 ) + 1 )
        enteredNums.append ( result )
        numerator = result

# prints the range only once the numerator has reached 1 and exits the loop
print ( *enteredNums )