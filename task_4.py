# Temperature Converter

class TemperatureConverter:

    def calsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    def fahrenheit_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
# Example usage
converter = TemperatureConverter()
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = converter.calsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_converted = converter.fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input}°F is equal to {celsius_converted}°C")
