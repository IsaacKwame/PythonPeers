"""
This program is meant to convert Fahrenheit temperature readings to celcius.
"""

print('Welcome to the Fahrenheit to Celsius conversion program')
ftemp = float(input('Please enter your  temperature reading in fahrenheit: ')) #accept fahrenheit temperature as float

ctemp = round(((ftemp - 32) *(5/9)), 2) #conversion and rounding of fahrenheit temperature 

print("Your temperature is: " + str(ctemp)+ " °C")  #Displaying the output