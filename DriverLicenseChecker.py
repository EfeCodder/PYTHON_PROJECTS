name = input("Please enter your name: ")

try:
    age = int(input("Please enter your age: "))

    if age <= 0 or age > 120:
        print("Please enter a valid age!")
    elif age < 18:
        print(f"Sorry {name}, you must be at least 18 years old to apply.")
    elif 18 <= age < 65:
        print(f"Congratulations {name}! You are eligible to apply for a driver's license.")
    else:
        print(f"Congratulations {name}! You are eligible to apply, but a medical health report is required for drivers over 65.")

except ValueError:
    print("Invalid input! Please enter your age as a number.")

input("\nPress Enter to exit...")