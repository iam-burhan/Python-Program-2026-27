# Unit 2 - Q5: User-defined modules and packages

# Import the entire module and access its functions through its name.
import arithmetic

# Import selected functions directly from the module.
from arithmetic import add, multiply

# Import the package. Selected functions are exposed in student/__init__.py.
from student import display_student, calculate_result


def main():
    print("Arithmetic using the complete module:")
    print("Subtraction:", arithmetic.subtract(20, 5))
    print("Division:", arithmetic.divide(20, 5))

    print("\nArithmetic using selected imported functions:")
    print("Addition:", add(20, 5))
    print("Multiplication:", multiply(20, 5))

    display_student("Aarav Sharma", "101", "MCA")
    marks = [78, 85, 91, 88]
    total, average = calculate_result(marks)
    print("\n--- Student Result ---")
    print("Marks:", marks)
    print("Total:", total)
    print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()
