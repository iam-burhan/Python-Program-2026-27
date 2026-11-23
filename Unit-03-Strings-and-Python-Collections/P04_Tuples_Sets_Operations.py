# Unit 3 - Q4: Tuples, sets and set operations

def main():
    # A tuple is ordered and immutable.
    roll_numbers = (101, 102, 103, 104, 105)
    print("Student roll number tuple:", roll_numbers)
    print("Tuple element at index 0:", roll_numbers[0])
    print("Tuple slice [1:4]:", roll_numbers[1:4])
    print("Tuple concatenation:", roll_numbers + (106, 107))

    # Sets store unique elements and do not guarantee display order.
    course_a = {101, 102, 103, 104}
    course_b = {103, 104, 105, 106}
    print("\nCourse A:", course_a)
    print("Course B:", course_b)

    print("Union:", course_a | course_b)
    print("Intersection:", course_a & course_b)
    print("A - B (difference):", course_a - course_b)
    print("Symmetric difference:", course_a ^ course_b)
    print("Course A is subset of union:", course_a.issubset(course_a | course_b))
    print("Union is superset of Course A:", (course_a | course_b).issuperset(course_a))

    course_a.add(107)
    print("After add(107):", course_a)
    course_a.discard(102)  # discard() does not raise an error if absent.
    print("After discard(102):", course_a)

    even_squares = {number ** 2 for number in range(1, 11)
                    if number % 2 == 0}
    print("Squares of even numbers from 1 to 10:", even_squares)


if __name__ == "__main__":
    main()
