FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp_input_str = input("Enter the temperature to convert: ")
temperature = float(temp_input_str)
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == 'F':
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted_temp}°C")
    break # Exit loop if conversion is successful

# Convert Fahrenheit to Celsius

elif unit == 'C':
# Convert Celsius to Fahrenheit
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted_temp}°F")
    break # Exit loop if conversion is successful
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


# def main():
#     while True:
#         try:

#         except ValueError:
#             print("Invalid temperature. Please enter a numeric value.")
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()
