# Unit 2 - Q2: *args, **kwargs and return statement

def calculate_result(student_name, *marks, **student_info):
    """
    *marks collects any number of subject marks into a tuple.
    **student_info collects extra named details into a dictionary.
    Return total, average and highest marks.
    """
    if not marks:
        raise ValueError("At least one subject mark is required.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Each mark must be between 0 and 100.")

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    return total, average, highest


def main():
    try:
        name = input("Enter student name: ").strip()
        if not name:
            raise ValueError("Student name cannot be empty.")

        roll_number = input("Enter roll number: ").strip()
        student_class = input("Enter class: ").strip()
        count = int(input("Enter number of subjects: "))

        if count <= 0:
            raise ValueError("Number of subjects must be greater than zero.")

        marks = []
        for index in range(count):
            mark = float(input(f"Enter marks for subject {index + 1}: "))
            marks.append(mark)

        # *marks passes all subject marks as separate positional arguments.
        # **student_info passes additional details as keyword arguments.
        total, average, highest = calculate_result(
            name, *marks, roll_number=roll_number, student_class=student_class
        )

        print("\n========== STUDENT RESULT ==========")
        print(f"Name        : {name}")
        print(f"Roll Number : {roll_number}")
        print(f"Class       : {student_class}")
        print(f"Total Marks : {total:.2f}")
        print(f"Average     : {average:.2f}")
        print(f"Highest     : {highest:.2f}")
        print("====================================")

    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
