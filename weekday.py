# Explanation: a program to determine whether it is currently the weekend or not.

# Task: Write a program that outputs whether or not today is a weekday. You will need to search the web to find how you work out what 
# day it is.

# Solution sources: A quick check of Google located almost exactly the answer I needed on StackOverflow. Both links are located in the 
# README file.

# Working notes: This program just required an imported library to function, and is the same as the code found on StackOverflow. I have
# amended the code from datetime.datetime datetime.date as this is what the official Python documentation recommended, although the 
# entry for datetime.datetime suggests that they are functionally identical. I have also amended the output messaging to match what 
# was posted on Moodle, and the name of the input variable.

import datetime

weekday = datetime.date.today ( ).weekday ( )

if weekday < 5:
    print ( "Yes, unfortunately today is a weekday.")

else :
    print ( "It is the weekend, yay!" )
