weight = int ( input(  "Enter your weight(kg): " ) )

height = int ( input ( "Enter your height(cm): " ) )

msg = "Your BMI is {}. BMI is the square of your height in metres, divided by your weight in kilograms."

bmi = weight / ( ( height / 100 ) * ( height / 100 ) )

print ( msg.format ( bmi ) )