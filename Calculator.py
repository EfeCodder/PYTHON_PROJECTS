try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2

    print(f"\nAddition Result: {add}")
    print(f"Subtraction Result: {subtract}")
    print(f"Multiplication Result: {multiply}")

    if num2 != 0:
        divide = num1 / num2
        remainder = num1 % num2
        print(f"Division Result: {divide}")
        print(f"Modulus (Remainder) Result: {remainder}")
    else:
        print("Division and Modulus Result: Cannot divide by zero!")

except ValueError:
    print("Invalid input! Please enter a valid number.")

input("\nPress enter to exit...")