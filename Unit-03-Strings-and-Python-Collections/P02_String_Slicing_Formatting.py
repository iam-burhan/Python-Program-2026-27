# Unit 3 - Q2: String slicing, indexing and formatting

def main():
    full_name = input("Enter student's full name: ").strip()
    email = input("Enter email address: ").strip()
    mobile = input("Enter mobile number: ").strip()

    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Please enter at least a first name and a last name.")
        return
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        print("Invalid email format.")
        return
    if not mobile.isdigit() or len(mobile) < 4:
        print("Mobile number must contain at least four digits.")
        return

    first_name = name_parts[0]
    last_name = name_parts[-1]
    username, domain = email.rsplit("@", 1)

    # Slicing with [::-1] returns the characters in reverse order.
    reversed_name = full_name[::-1]
    last_four = mobile[-4:]

    print("\n--- Student Information ---")
    print(f"Full Name : {full_name}")
    print(f"First Name: {first_name}")
    print(f"Last Name : {last_name}")
    print(f"Reversed  : {reversed_name}")
    print(f"Username  : {username}")
    print(f"Domain    : {domain}")
    print(f"Mobile    : ******{last_four}")

    # Positive indexing starts at 0; negative indexing starts at -1.
    print("\nIndexing demonstration:")
    print("First character (index 0):", full_name[0])
    print("Last character (index -1):", full_name[-1])

    # Other formatting techniques.
    print("format() example: Name: {}, Email: {}".format(full_name, email))
    print("Percent formatting example: Name: %s | Last four digits: %s" %
          (full_name, last_four))


if __name__ == "__main__":
    main()
