# === Import modules ===
from Conversions import Temperature, Length
from Volume import Volume
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
        print("3. Time Conversions")
        print("4. Mass Conversions")
        print("5. Back to Main Menu")

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
            print("\n--- Time Conversions ---")
            print("1. Hours to Minutes")
            print("2. Minutes to Hours")
            print("3. Seconds to Minutes")
            print("4. Minutes to Seconds")
            print("5. Back")
            sub = input("Enter your choice: ")
            if sub == "1":
                h = float(input("Enter Hours: "))
                print("Minutes:", Time.hours_to_minutes(h))
            elif sub == "2":
                m = float(input("Enter Minutes: "))
                print("Hours:", Time.minutes_to_hours(m))
            elif sub == "3":
                s = float(input("Enter Seconds: "))
                print("Minutes:", Time.seconds_to_minutes(s))
            elif sub == "4":
                m = float(input("Enter Minutes: "))
                print("Seconds:", Time.minutes_to_seconds(m))
            elif sub == "5":
                continue
            else:
                print("Invalid choice!")

        elif choice == "4":
            print("\n--- Mass Conversions ---")
            print("1. Kilograms to Pounds")
            print("2. Pounds to Kilograms")
            print("3. Grams to Ounces")
            print("4. Ounces to Grams")
            print("5. Back")
            sub = input("Enter your choice: ")
            if sub == "1":
                kg = float(input("Enter Kilograms: "))
                print("Pounds:", Mass.kilograms_to_pounds(kg))
            elif sub == "2":
                p = float(input("Enter Pounds: "))
                print("Kilograms:", Mass.pounds_to_kilograms(p))
            elif sub == "3":
                g = float(input("Enter Grams: "))
                print("Ounces:", Mass.grams_to_ounces(g))
            elif sub == "4":
                o = float(input("Enter Ounces: "))
                print("Grams:", Mass.ounces_to_grams(o))
            elif sub == "5":
                continue
            else:
                print("Invalid choice!")

        elif choice == "5":
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
    while True:
        print("----Volume Calculations----\n")
        print("Enter Choice to Proceed")
        print("1. Volume of Sphere")
        print("2. Volume of Cylinder")
        print("3. Volume of Cone")
        print("4. Volume of Cube")
        print("5. Volume of Cuboid")
        print("6. Volume of Hemisphere")
        print("7. Back to Main Menu");
        
        choice = int(input("\nEnter Your choice: "))

        if(choice == 1):
            radius = float(input("\nEnter the radius: "))
            print(f"Volume of Sphere of radius({radius}) = {Volume.sphere(radius)}\n")

        elif(choice == 2):
            radius = float(input("\nEnter the radius: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cylinder of radius({radius}) and height({height}) = {Volume.cylinder(radius,height)}\n")

        elif(choice == 3):
            radius = float(input("\nEnter the radius: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cone of radius({radius}) and height({height}) = {Volume.cone(radius,height)}\n")

        elif(choice == 4):
            side = float(input("\nEnter Length of the side:"))
            print(f"Volume of Cube of side({side}) = {Volume.cube(side)}\n")

        elif(choice == 5):
            length = float(input("\nEnter the length: "))
            breadth = float(input("Enter the breadth: "))
            height = float(input("Enter the height: "))
            print(f"Volume of Cuboid of length({radius}), breadth({breadth}) and height({height}) = {Volume.cuboid(length,breadth,height)}\n")

        elif(choice == 6):
            radius = float(input("\nEnter the radius: "))
            print(f"Volume of Hemisphere of radius({radius}) = {Volume.hemisphere(radius)}\n")

        elif(choice == 7):
            print("Thank You...\n")
            break;
        else:
            print("Invalid Choice\n")


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
