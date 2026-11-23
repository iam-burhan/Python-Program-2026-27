# Unit 3 - Q3: List operations and list comprehension

def main():
    try:
        count = int(input("How many integers do you want in the list? "))
        if count <= 0:
            raise ValueError("Enter a number greater than zero.")

        numbers = []
        for index in range(count):
            numbers.append(int(input(f"Enter integer {index + 1}: ")))

        print("\nOriginal list:", numbers)

        # Demonstrate append(), extend(), insert(), remove(), pop().
        numbers.append(100)
        numbers.extend([200, 300])
        numbers.insert(0, 50)
        print("After append, extend and insert:", numbers)

        value_to_remove = int(input("Enter a value to remove (or a value not present): "))
        if value_to_remove in numbers:
            numbers.remove(value_to_remove)
            print("After remove:", numbers)
        else:
            print("Value not found; remove() was not called.")

        removed_item = numbers.pop() if numbers else None
        print("Popped item:", removed_item)
        print("After pop:", numbers)

        ascending = sorted(numbers)
        descending = sorted(numbers, reverse=True)
        print("Ascending:", ascending)
        print("Descending:", descending)
        print("Maximum:", max(numbers) if numbers else "List is empty")
        print("Minimum:", min(numbers) if numbers else "List is empty")
        print("Sum:", sum(numbers))

        print("Concatenation:", numbers + [400, 500])
        print("Repetition:", numbers * 2)
        if numbers:
            print("First element by indexing:", numbers[0])
        search_value = int(input("Enter a value to search: "))
        print("Membership test:", search_value in numbers)

        # List comprehensions create new lists from an iterable.
        print("Even numbers:", [n for n in numbers if n % 2 == 0])
        print("Odd numbers:", [n for n in numbers if n % 2 != 0])
        print("Squares:", [n ** 2 for n in numbers])

        # sort() changes the list in place; reverse() reverses its current order.
        numbers.sort()
        print("After sort():", numbers)
        numbers.reverse()
        print("After reverse():", numbers)

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
