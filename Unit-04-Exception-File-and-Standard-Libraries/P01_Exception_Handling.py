# Unit 4 - Q1: Exception handling

def main():
    # Multiple except blocks handle different error types.
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        print("Division result:", numerator / denominator)

        values = [10, 20, 30]
        index = int(input("Enter a list index (0 to 2): "))
        print("List value:", values[index])

    except ZeroDivisionError:
        print("Error: Division by zero is not permitted.")
    except ValueError:
        print("Error: Please enter valid numerical input.")
    except IndexError:
        print("Error: The requested list index does not exist.")
    else:
        # else runs only when the try block completes without an exception.
        print("No exception occurred in the try block.")
    finally:
        # finally runs whether an exception occurred or not.
        print("The first exception-handling demonstration has finished.")

    # raise is used to deliberately generate an exception for an invalid age.
    try:
        age = int(input("\nEnter your age: "))
        if age < 18:
            raise ValueError("Age must be 18 or above.")
    except ValueError as error:
        print("Age validation error:", error)
    else:
        print("Age accepted. You are 18 or older.")
    finally:
        print("Age validation completed.")


if __name__ == "__main__":
    main()
