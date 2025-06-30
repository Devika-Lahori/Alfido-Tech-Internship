def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    while True:
        print("\n Temperature Converter")
        print("-------------------------")
        print("1. Celsius to Fahrenheit & Kelvin")
        print("2. Fahrenheit to Celsius & Kelvin")
        print("3. Kelvin to Celsius & Fahrenheit")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            c = float(input("Enter temperature in Celsius: "))
            print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f} °F")
            print(f"Kelvin: {celsius_to_kelvin(c):.2f} K")

        elif choice == '2':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"Celsius: {fahrenheit_to_celsius(f):.2f} °C")
            print(f"Kelvin: {fahrenheit_to_kelvin(f):.2f} K")

        elif choice == '3':
            k = float(input("Enter temperature in Kelvin: "))
            print(f"Celsius: {kelvin_to_celsius(k):.2f} °C")
            print(f"Fahrenheit: {kelvin_to_fahrenheit(k):.2f} °F")

        elif choice == '4':
            print("Program Ended. Stay cool!")
            break

        else:
            print("Invalid input. Try again!")

        again = input("\nDo you want to convert another temperature? (yes/no): ").strip().lower()
        if again != 'yes':
            print(" Goodbye! Take care.")
            break

temperature_converter()
