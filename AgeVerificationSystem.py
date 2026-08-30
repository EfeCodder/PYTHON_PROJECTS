name = input("Please enter your name: ")

try:
    age = int(input("Please enter your age: "))

    if age <= 0 or age > 120:
        print("Please enter a valid age!")
    elif age < 18:
        print(f"Sorry {name}, access denied! You must be at least 18 years old.")
    else:
        print(f"Welcome {name}! Access granted to the system.")
    
except ValueError:
    print("Invalid input! Please enter your age as a number.")

input("\nPress enter to exit...")