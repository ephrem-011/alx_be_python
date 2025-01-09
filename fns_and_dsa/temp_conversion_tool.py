FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*(FAHRENHEIT_TO_CELSIUS_FACTOR)
def convert_to_fahrenheit(celsius):
    return (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
def main():
    temp_input=float(input("Enter the temperature to convert: "))
    while True:
        conv_input=str(input("Is this temperature in Celsius or Fahrenheit? (C/F): ")).lower()
        match conv_input:
            case 'c':
                print (convert_to_fahrenheit(temp_input))
                break
            case 'f':
                print (convert_to_celsius(temp_input))
                break
            case _:
                print("Wrong input")
                continue

if __name__ == "__main__":
    main()