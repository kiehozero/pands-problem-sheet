# Explanation: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

# Task:

# Sources: The README contains likes from HackerNoon and GeeksForGeeks which were good introductions on the topic.

# Working Notes: I traced out the basic skeleton of this program as a function which simply returns the input and 
# output values inside an f-string, the real challenge here was actually working out how to do the mathematical part
# of the task.


# error handling? if number is less than 0, repeat

def sqrt ( number ):

    squared = number * 3    
    return ( f"The square root of { number } is approximately { squared }." )

floater = float ( 
    input (
        "Please enter a positive number: "
    )
)
print (
     sqrt ( floater )
)
