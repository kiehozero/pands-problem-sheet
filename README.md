# pands-problem-sheet
A repository for markable work on 52167 Programming and Scripting

## Week 2
- Task: Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py. The inputs are the person's height in centimetres and weight in kilograms.
The output their BMI (You may need to look up how this is calculated);
- File submitted: [BMI](/bmi.py);
- Solution source was the [NHS BMI calculator](https://www.nhs.uk/live-well/healthy-weight/bmi-calculator/).
- Working notes: I amended the tool to include the {:.2f} information at line 7 to restrict decimal places after reviewing the lecture material in week 4. I have also used integers over floats, as I don't anticipate most people knowing their height and weight to a gram or millimetre granularity.

## Week 3
- Task: Write a program that asks a user to input a string and outputs every second letter in reverse order;
- File submitted: [secondstring](/secondstring.py);
- Solution sources were [W3Schools](https://www.w3schools.com/python/python_howto_reverse_string.asp) and ultimately [W3Schools' Slice Function](https://www.w3schools.com/python/ref_func_slice.asp) page;
Working notes: I couldn't get the [::-1] syntax that W3 was giving me to work without also defining a function, so I've determined the start point of the function by calculating the length of the string as inputLen and setting the end point as zero. I also initially set this as 1 but it then skipped the final character.

## Week 4
- Task: Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.
- File submitted: [Collatz](/collatz.py);
- Solution sources: [W3Schools Append Method](https://www.w3schools.com/python/ref_list_append.asp), [Data Science Parichay](https://datascienceparichay.com/article/python-print-list/)
- Working notes: The first problem I encountered as usual was not ensuring that entries were integers. I then had a couple of phases of moving the append and the next input in and out of various parts of the loop. I also misunderstood the original request that the user should input the new number at each stage rather than calculating everything from an initial submission. After getting a horrific infinite loop on the second try (see commit history), I realised that I needed to define the output as the next input, as well as adding the original user submission to the list, so I swapped the first two lines of code around and removed the final lines of code that repeated the number 1 being appended. After Googling for a solution to printing the items of a list separately but on the same line instead of all within square brackets, I used the asterisk as outlined in the DataScienceParichay link (heading 'Using * operator to unpack the list') above.

## Week 5
- Task: Write a program that outputs whether or not today is a weekday.
- File submitted: 
- Solution sources:
- Working notes:

## Week 6
- Task:
- File submitted: 
- Solution sources:
- Working notes:

## Week 7
- Task:
- File submitted: 
- Solution sources:
- Working notes:

## Week 8
- Task:
- File submitted: 
- Solution sources:
- Working notes:

## Week 9
- Task:
- File submitted: 
- Solution sources:
- Working notes:

## Week 10
- Task:
- File submitted: 
- Solution sources:
- Working notes: