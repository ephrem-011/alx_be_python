def convert_to_celsius(fahrenheit):
    return (fahrenheit-32)*(5/9)
def convert_to_fahrenheit(celsius):
    return (celsius*9/5)+32
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