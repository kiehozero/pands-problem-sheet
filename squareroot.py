# Explanation: A program that estimates the square root of a given number

# Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

# Sources: The README contains likes from HackerNoon, RealPython and GeeksForGeeks which were vital for me to get any results
# on this particular problem.

# Working Notes: I traced out the basic skeleton of this program as a function which simply returns the input and output 
# values inside an f-string, the real challenge here was actually working out how to do the mathematical part of the task as 
# an approximation of how a person would do this using mental arithmetic, rather than calculating the exact number. The code 
# below is pretty much an exact copy of what is found at the GeeksForGeeks link in the README, I've just changed the name of 
# variables to make it easier to read as a broke down the code to understand what each  line is doing, and I've also removed 
# a counter that was redundant for this task. I then used the RealPython link in the README to work out how to round to a 
# single decimal place, after first trying to use string formatting and the round function, both of which returned 3.9 
# instead of 3.8. I finally changed the tolerance back to 0.1, as the original GeeksForGeeks link had one, and I got 3.8. 
# I'm sure there is a much easier and better way of doing this, such as keeping the square-root and the rounding functions 
# separate, but I am officially tapping out on this problem.

from math import floor

def sqrt(number):

    guess = number
    tolerance = 0.1
 
    while (tolerance) :
        # The original number is divided by the current guess, and the result added to that guess and halved
        root = 0.5 * (guess + (number / guess))
 
        # This part checks that the tolerance threshold has been reached, and breaks the loop if it has
        if (abs(root - guess) < tolerance) :
            break
 
        # Otherwise, the root is updated to the current output of guess, to begin the loop again at line 27
        guess = root

    # this part is taken from the Rounding Down section of the Real Python link in the README, where it is defined
    # as a separate function, their logic is simply to shift the decimal place across (line 38) and then back 
    # again (line 39)

    multiplier = 10 ** 1
    out = floor(root * multiplier) / multiplier
    return f"The square root of {number} is approximately {out}."

floater = float( 
    input(
        "Please enter a positive number: "
    )
)

print(
     sqrt(floater)
)
