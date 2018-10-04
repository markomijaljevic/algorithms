import sys

def FahrenheitToCelsiusCalculator(temperature):
    celsius = (float(temperature) - 32 ) / (9/5)
    print("Fahrenheit value is ",temperature, ", and Celsius Value is ",celsius)
    
print("---------------------------------\n")
print("Fahrenheit to Celsius Calculator!\n")
print("---------------------------------\n")

while True:
    try:
        temperature = float(input("Please input temperature in Fahrenheit (use dot '.' for decimal point):  "))
    except ValueError:
        print("--------------------------------\n")
        print("Please insert only numeric value\n")
        print("--------------------------------\n")
        continue;

    FahrenheitToCelsiusCalculator(temperature)
    if input("Input 0 to start over:  ") == "0": 
        continue;
    break;
    