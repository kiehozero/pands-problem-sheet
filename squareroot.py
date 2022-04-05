# Explanation: A program that estimates the square root of a given number

# Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

# Sources: The README contains likes from HackerNoon and GeeksForGeeks which were good introductions on the topic.

# Working Notes: I traced out the basic skeleton of this program as a function which simply returns the input and 
# output values inside an f-string, the real challenge here was actually working out how to do the mathematical part
# of the task.


# error handling? if number is less than 0, repeat

def sqrt(number):

    x = int(number)

    squared = int(number * number)
    return (f"The square root of {x} is approximately {squared}.")

floater = float( 
    input(
        "Please enter a positive number: "
    )
)

print(
     sqrt(floater)
)
