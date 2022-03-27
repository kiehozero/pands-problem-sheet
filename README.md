# pands-problem-sheet
A repository for markable work on 52167 Programming and Scripting

## Week 2
- Task: Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py. The inputs are the person's height in centimetres and weight in kilograms.
The output their BMI (You may need to look up how this is calculated);
- File submitted: [BMI](/bmi.py);
- Source was the [NHS BMI calculator](https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/).
- Working notes: I amended the tool to include the {:.2f} information at line 7 to restrict decimal places after reviewing the lecture material in week 4. I have also used integers over floats, as I don't anticipate most people knowing their height and weight to a gram or millimetre granularity.

## Week 3
- Task: Write a program that asks a user to input a string and outputs every second letter in reverse order;
- File submitted: [secondstring](/secondstring.py);
- Sources were [W3Schools](https://www.w3schools.com/python/python_howto_reverse_string.asp) and ultimately [W3Schools' Slice Function](https://www.w3schools.com/python/ref_func_slice.asp) page;
Working notes: I couldn't get the [::-1] syntax that W3 was giving me to work without also defining a function, so I've determined the start point of the function by calculating the length of the string as inputLen and setting the end point as zero. I also initially set this as 1 but it then skipped the final character.

## Week 4
- Task: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
- File submitted: [Collatz](/collatz.py);
- Sources: [W3Schools Append Method](https://www.w3schools.com/python/ref_list_append.asp), [Data Science Parichay](https://datascienceparichay.com/article/python-print-list/)
- Working notes: The first problem I encountered as usual was not ensuring that entries were integers. I then had a couple of phases of moving the append and the next input in and out of various parts of the loop. I also misunderstood the original request that the user should input the new number at each stage rather than calculating everything from an initial submission. After getting a horrific infinite loop on the second try (see commit history), I realised that I needed to define the output as the next input, as well as adding the original user submission to the list, so I swapped the first two lines of code around and removed the final lines of code that repeated the number 1 being appended. After Googling for a solution to printing the items of a list separately but on the same line instead of all within square brackets, I used the asterisk as outlined in the DataScienceParichay link (heading 'Using * operator to unpack the list') above.

## Week 5
- Task: Write a program that outputs whether or not today is a weekday.
- File submitted: [Weekday](/weekday.py)
- Sources:
    [StackOverflow](https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python)
    [Python's date library docs](https://docs.python.org/3/library/datetime.html#datetime.date.weekday)
- Working notes: This program just required an imported library to function, and is the same as the code found on StackOverflow. I have amended the code from datetime.datetime datetime.date as this is what the official Python documentation recommended, although the entry for datetime.datetime suggests that they are functionally identical. I have also amended the output messaging to match what was posted on Moodle, and the name of the input variable.

## Week 6
- Task: Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

- File submitted: [Square Root](/squareroot.py)
- Sources:
    [GeeksForGeeks: Square Roots](https://www.geeksforgeeks.org/how-to-calculate-a-square-root/)
    [HackerNoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo)
    [GeeksForGeeks: Newton's Method](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)
- Working notes:

## Week 7
- Task: Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making. The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
- File submitted: [Es](es.py)
- Sources:
    [GeeksForGeeks: Count Occurrences](https://www.geeksforgeeks.org/python-count-occurrences-of-a-character-in-string/ )
    [StackOverflow thread on sys.argv](https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python#7439162)
    [Moby Dick txt file](https://gist.github.com/StevenClontz/4445774)
- Working notes: The first part of the solution was bringing in the file name as part of the command, rather than using a user input or hard-coding the filename into the sources. I found a simple solution using the sys.argv command that allowed this, then I just had a to set up a one-line .txt file to test it. 

The GeeksForGeeks article above highlighted three methods for counting characters; I used what I considered to be the cleanest method of the three. The first method was a 'for' loop, while the third method required importing a function that achieved the same result as the second method, which is a built-in function, and so seemed the most obvious to use.

An error that I noticed was when I was testing on the Moby Dick txt file. After running another file, I realised that my program was case-sensitive. Adding the lower() function was enough to get this counting correctly, by storing a lower-case-only version of the file as a separate variable.

## Week 8
- Task: Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
- File submitted: [Plot Task](plottask.py)
- Sources: I was able to complete the bulk of this task using the lecture slides and the accompanying further reading material. I did some extra research into more advanced styling options, namely:
    The W3Schools tutorial on [Matplotlib markers](https://www.w3schools.com/python/matplotlib_markers.asp). I also used the subsequent links in that tutorial for lines and grids;
    The W3Schools tutorial on [Matplotlib titles](https://www.w3schools.com/python/matplotlib_labels.asp);
    The NumPy documentation for the [append function](https://numpy.org/doc/stable/reference/generated/numpy.append.html), which I ultimately could not get to work;
    The Matplotlib documentation for the [legend property](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html).

- Working notes:
