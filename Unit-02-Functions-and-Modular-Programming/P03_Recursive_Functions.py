# Unit 2 - Q3: Recursive functions

def factorial(number):
    """Return factorial using recursion."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if number in (0, 1):       # Base case stops the recursion.
        return 1
    return number * factorial(number - 1)


def fibonacci(number_of_terms):
    """Return a Fibonacci sequence containing the requested number of terms."""
    if number_of_terms < 0:
        raise ValueError("Number of terms cannot be negative.")
    if number_of_terms == 0:
        return []
    if number_of_terms == 1:
        return [0]

    previous_terms = fibonacci(number_of_terms - 1)
    next_value = previous_terms[-1] + (
        previous_terms[-2] if len(previous_terms) > 1 else 0
    )
    return previous_terms + [next_value]


def main():
    try:
        value = int(input("Enter a non-negative integer for factorial: "))
        terms = int(input("Enter number of Fibonacci terms: "))

        print(f"Factorial of {value} = {factorial(value)}")
        print(f"Fibonacci series ({terms} terms) =", fibonacci(terms))

    except ValueError as error:
        print("Input error:", error)
        print("Please enter valid non-negative integers.")


if __name__ == "__main__":
    main()
