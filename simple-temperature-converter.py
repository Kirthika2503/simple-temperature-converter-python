# a simple temperature converter

temperature = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C or F): " ).upper()

result = None 
converted_unit = None

if unit == "C":
   result = round((temperature * 9/5) + 32, 2)
   converted_unit = "F"
   
elif unit == "F":
   result = round((temperature - 32) * 5/9, 2)
   converted_unit = "C"

else: 
   print(f"{unit} is invalid !")
   exit()

if result is not None:
  print(f"The temperature is: {result} {converted_unit}")

