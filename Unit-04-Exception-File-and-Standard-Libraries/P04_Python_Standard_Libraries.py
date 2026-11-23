# Unit 4 - Q4: Python standard libraries (math, random, datetime)

import math
import random
from datetime import date, datetime


def demonstrate_math():
    number = float(input("Enter a non-negative number for math operations: "))
    if number < 0:
        print("Square root requires a non-negative number.")
        return

    integer_for_factorial = int(input("Enter a non-negative integer for factorial: "))
    if integer_for_factorial < 0:
        print("Factorial requires a non-negative integer.")
        return

    exponent = float(input("Enter a power/exponent: "))
    print("\n--- math module ---")
    print("Square root:", math.sqrt(number))
    print("Factorial:", math.factorial(integer_for_factorial))
    print("Power (number ** exponent):", math.pow(number, exponent))
    print("Ceiling:", math.ceil(number))
    print("Floor:", math.floor(number))


def demonstrate_random():
    items = ["Python", "Java", "SQL", "Power BI"]
    print("\n--- random module ---")
    print("Random integer from 1 to 100:", random.randint(1, 100))
    print("Random item:", random.choice(items))
    random.shuffle(items)  # shuffle() changes the list in place.
    print("Shuffled list:", items)


def demonstrate_datetime():
    current = datetime.now()
    print("\n--- datetime module ---")
    print("Current date and time:", current.strftime("%Y-%m-%d %H:%M:%S"))
    print("Day:", current.day)
    print("Month:", current.month)
    print("Year:", current.year)

    first_text = input("Enter first date (YYYY-MM-DD): ")
    second_text = input("Enter second date (YYYY-MM-DD): ")
    first_date = date.fromisoformat(first_text)
    second_date = date.fromisoformat(second_text)
    difference = abs((second_date - first_date).days)
    print("Difference between dates:", difference, "days")


def main():
    try:
        demonstrate_math()
        demonstrate_random()
        demonstrate_datetime()
    except ValueError as error:
        print("Invalid input or date:", error)


if __name__ == "__main__":
    main()
