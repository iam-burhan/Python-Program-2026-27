# Unit 4 - Q3: File methods and file-related exception handling

FILE_NAME = "student.txt"


def main():
    try:
        # Create a sample file only if it does not already exist.
        try:
            with open(FILE_NAME, "x", encoding="utf-8") as sample:
                sample.write("Name: Aarav\nRoll Number: 101\nCourse: MCA\n")
        except FileExistsError:
            pass

        file = open(FILE_NAME, "r", encoding="utf-8")
        try:
            print("File name:", file.name)
            print("File mode:", file.mode)

            print("\nread() - reads the complete content:")
            print(file.read())

            print("Current position after read():", file.tell())

            # seek(0) moves the file pointer back to the beginning.
            file.seek(0)
            print("\nreadline() - reads one line:")
            print(file.readline(), end="")
            print("Position after readline():", file.tell())

            file.seek(0)
            print("\nreadlines() - returns all lines as a list:")
            print(file.readlines())

        finally:
            file.close()
            print("\nFile closed:", file.closed)

    except FileNotFoundError:
        print("Error: The requested file was not found.")
    except PermissionError:
        print("Error: Permission denied while accessing the file.")
    except OSError as error:
        print("Other file-related error:", error)
    else:
        print("File operations completed successfully.")
    finally:
        print("File-method demonstration finished.")


if __name__ == "__main__":
    main()
