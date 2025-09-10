# === Import modules ===
from Conversions import Temperature, Length
# Other modules would be imported similarly


# === Menu Functions for Each Module ===

def area_menu():
    print("\n--- Area Calculations ---")
    # Placeholder (to be implemented later)
    pass


def conversions_menu():
    while True:
        print("\n--- Conversions ---")
        print("1. Temperature Conversions")
        print("2. Length Conversions")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Temperature Conversions ---")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            print("5. Back")
            sub = input("Enter your choice: ")
            if sub == "1":
                c = float(input("Enter Celsius: "))
                print("Fahrenheit:", Temperature.celsius_to_fahrenheit(c))
            elif sub == "2":
                f = float(input("Enter Fahrenheit: "))
                print("Celsius:", Temperature.fahrenheit_to_celsius(f))
            elif sub == "3":
                c = float(input("Enter Celsius: "))
                print("Kelvin:", Temperature.celsius_to_kelvin(c))
            elif sub == "4":
                k = float(input("Enter Kelvin: "))
                print("Celsius:", Temperature.kelvin_to_celsius(k))
            elif sub == "5":
                continue
            else:
                print("Invalid choice!")

        elif choice == "2":
            print("\n--- Length Conversions ---")
            print("1. Meters to Feet")
            print("2. Feet to Meters")
            print("3. Kilometers to Miles")
            print("4. Miles to Kilometers")
            print("5. Back")
            sub = input("Enter your choice: ")
            if sub == "1":
                m = float(input("Enter Meters: "))
                print("Feet:", Length.meters_to_feet(m))
            elif sub == "2":
                f = float(input("Enter Feet: "))
                print("Meters:", Length.feet_to_meters(f))
            elif sub == "3":
                km = float(input("Enter Kilometers: "))
                print("Miles:", Length.kilometers_to_miles(km))
            elif sub == "4":
                miles = float(input("Enter Miles: "))
                print("Kilometers:", Length.miles_to_kilometers(miles))
            elif sub == "5":
                continue
            else:
                print("Invalid choice!")

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def interest_menu():
    print("\n--- Interest Calculations ---")
    # Placeholder
    pass


def number_system_menu():
    print("\n--- Number System Operations ---")
    # Placeholder
    pass


def statistics_menu():
    print("\n--- Statistics ---")
    # Placeholder
    pass


def trignometry_menu():
    print("\n--- Trignometry ---")
    # Placeholder
    pass


def vector_menu():
    print("\n--- Vector Operations ---")
    # Placeholder
    pass


def volume_menu():
    print("\n--- Volume Calculations ---")
    # Placeholder
    pass


# === Main App ===

def main():
    while True:
        print("\n=== Scientific Calculator ===")
        print("1. Area")
        print("2. Conversions")
        print("3. Interest")
        print("4. Number System")
        print("5. Statistics")
        print("6. Trignometry")
        print("7. Vector")
        print("8. Volume")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            area_menu()
        elif choice == "2":
            conversions_menu()
        elif choice == "3":
            interest_menu()
        elif choice == "4":
            number_system_menu()
        elif choice == "5":
            statistics_menu()
        elif choice == "6":
            trignometry_menu()
        elif choice == "7":
            vector_menu()
        elif choice == "8":
            volume_menu()
        elif choice == "9":
            print("Nandriii... Meendum Varuga...!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
