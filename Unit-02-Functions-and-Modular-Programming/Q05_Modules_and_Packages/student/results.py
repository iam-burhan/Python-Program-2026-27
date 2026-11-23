# Package module: student results

def calculate_result(marks):
    if not marks:
        raise ValueError("At least one mark is required.")
    total = sum(marks)
    average = total / len(marks)
    return total, average
