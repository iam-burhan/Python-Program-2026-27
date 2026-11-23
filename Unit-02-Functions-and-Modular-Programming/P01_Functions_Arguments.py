# Unit 2 - Q1: Functions and Function Arguments

def add(a, b, operation="addition"):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b, operation="subtraction"):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b, operation="multiplication"):
    """Return the product of two numbers."""
    return a * b


def divide(a, b, operation="division"):
    """Return the quotient; division by zero is not allowed."""
    if b == 0:
        raise ZeroDivisionError("The second number cannot be zero for division.")
    return a / b


def main():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        # Positional arguments: values are matched by their position.
        print("\nUsing positional arguments:")
        print("Addition:", add(first, second))

        # Keyword arguments: parameter names are written explicitly.
        print("\nUsing keyword arguments:")
        print("Subtraction:", subtract(a=first, b=second))
        print("Multiplication:", multiply(b=second, a=first))

        # The optional operation parameter has a default value.
        print("\nDefault operation label:", add(first, second))
        print("Division:", divide(a=first, b=second))

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
