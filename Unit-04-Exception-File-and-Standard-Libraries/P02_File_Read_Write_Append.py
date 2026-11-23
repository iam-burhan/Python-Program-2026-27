# Unit 4 - Q2: File handling - write, read and append

FILE_NAME = "student.txt"


def main():
    # 'w' creates the file or replaces its previous contents.
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            name = input("Enter student name: ").strip()
            roll_number = input("Enter roll number: ").strip()
            course = input("Enter course: ").strip()
            file.write(f"Name: {name}\n")
            file.write(f"Roll Number: {roll_number}\n")
            file.write(f"Course: {course}\n")

        # Read and display the complete file contents.
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            print("\nComplete file contents:")
            print(file.read())

        # 'a' adds new data at the end without deleting old records.
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write("\n--- Additional Student Record ---\n")
            file.write("Name: Meera Patel\n")
            file.write("Roll Number: 102\n")
            file.write("Course: MCA\n")

        # Read line by line and display all lines.
        file = open(FILE_NAME, "r", encoding="utf-8")
        try:
            print("File contents line by line:")
            for line in file:
                print(line, end="")
        finally:
            # Explicit close() demonstrates how to close a file manually.
            file.close()
            print("\nFile closed:", file.closed)

    except OSError as error:
        print("File operation failed:", error)


if __name__ == "__main__":
    main()
