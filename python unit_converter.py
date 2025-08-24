def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("🌍 Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Choose conversion (1-4): ")

try:
    if choice == '1':
        km = float(input("Enter kilometers: "))
        miles = km_to_miles(km)
        print("Kilometers:", km)
        print("Miles:", round(miles, 2))

    elif choice == '2':
        miles = float(input("Enter miles: "))
        km = miles_to_km(miles)
        print("Miles:", miles)
        print("Kilometers:", round(km, 2))

    elif choice == '3':
        c = float(input("Enter Celsius: "))
        f = c_to_f(c)
        print("Celsius:", c)
        print("Fahrenheit:", round(f, 2))

    elif choice == '4':
        f = float(input("Enter Fahrenheit: "))
        c = f_to_c(f)
        print("Fahrenheit:", f)
        print("Celsius:", round(c, 2))

    else:
        print("❌ Invalid choice.")

except ValueError:
    print("❌ Please enter a valid number.")