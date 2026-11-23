# Unit 3 - Q5: Dictionaries, comprehension and nested collections

def main():
    employee = {
        "employee_id": 1001,
        "name": "Aarav Sharma",
        "department": "IT",
        "salary": 45000
    }

    print("Original employee:", employee)

    # Add a new key, update an existing key and delete a key.
    employee["email"] = "aarav@example.com"
    employee["salary"] = 52000
    print("After adding email and updating salary:", employee)

    removed_value = employee.pop("email", None)
    print("Deleted email value:", removed_value)

    print("\nDictionary keys:", list(employee.keys()))
    print("Dictionary values:", list(employee.values()))
    print("Key-value pairs:")
    for key, value in employee.items():
        print(f"{key}: {value}")

    # Search using employee ID.
    search_id = int(input("\nEnter employee ID to search: "))
    if employee.get("employee_id") == search_id:
        print("Employee found:", employee)
    else:
        print("Employee ID not found.")

    # A nested dictionary stores multiple employee records.
    employees = {
        1001: {"name": "Aarav", "department": "IT", "salary": 52000},
        1002: {"name": "Diya", "department": "HR", "salary": 38000},
        1003: {"name": "Kabir", "department": "Finance", "salary": 61000}
    }

    threshold = float(input("Enter minimum salary threshold: "))
    high_earners = {
        emp_id: details
        for emp_id, details in employees.items()
        if details["salary"] > threshold
    }
    print("\nEmployees earning above", threshold, ":")
    for emp_id, details in high_earners.items():
        print(emp_id, details)


if __name__ == "__main__":
    main()
