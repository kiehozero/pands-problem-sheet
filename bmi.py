# Explanation: A simple tool to allow for calculation of a user's BMI using their height and weight data.

# Task: Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py. The inputs 
# are the person's height in centimetres and weight in kilograms. The output their BMI (You may need to 
# look up how this is calculated).

# Sources: To create this program, the existing lecture notes were sufficient. The exact calcuation 
# is taken from the NHS  BMI calculator that is linked in the README.

# Working notes: I amended the tool to include the {:.2f} information at line 7 to restrict decimal places 
# after reviewing the lecture material in week 4. I have also used integers over floats, as I don't 
# anticipate most people knowing their height and weight to a gram or millimetre granularity.

weight = int ( input ( "Enter your weight(kg): " ) )

height = int ( input ( "Enter your height(cm): " ) )

msg = "Your BMI is {:.2f}. BMI is the square of your height in metres, divided by your weight in kilograms."

bmi = weight / ( ( height / 100 ) * ( height / 100 ) )

print ( msg.format ( bmi ) )