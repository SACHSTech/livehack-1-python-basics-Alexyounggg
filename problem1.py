'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Convert the temperature from celsius to fahrenheit 

Author:	Young.A

Created:	7/12/2020
-----------------------------------------------------------------------------
'''

print ("*****Welcome to the Celsius Converter Program*****")

# Allow user to input temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Convert the temperature from Celsius to Fahrenhiet 
fahrenheit = 9/5*celsius + 32

# Output the temperature in Fahrenheit
print("The temperature is " +str(fahrenheit)+ " Fahrenheit.")


