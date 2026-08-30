try:
    month = int(input("Please enter a month number (1-12): "))

    match month:
        case 12 | 1 | 2:
            season = "Winter"
        case 3 | 4 | 5:
            season = "Spring"
        case 6 | 7 | 8:
            season = "Summer"
        case 9 | 10 | 11:
            season = "Autumn"
        case _:
            season = None

    if season:
        print(f"Month {month} is in {season}.")
    else:
        print("Invalid month number! Please enter a number between 1 and 12.")
    
except ValueError:
    print("Invalid input! Please enter a valid number.")

input("\nPress enter to exit...")