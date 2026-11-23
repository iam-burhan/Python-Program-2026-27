# Unit 2 - Q4: Scope, lifetime and lambda functions

# A global variable is created outside all functions.
global_count = 10


def demonstrate_scope():
    # 'global' allows this function to reassign the global variable.
    global global_count
    local_message = "I exist only while this function is executing."
    print("Inside function - global_count:", global_count)
    print("Inside function - local_message:", local_message)
    global_count += 1


def main():
    print("Before function call - global_count:", global_count)
    demonstrate_scope()
    print("After function call - global_count:", global_count)

    # local_message is local to demonstrate_scope and cannot be accessed here.
    # Its lifetime ends when demonstrate_scope() finishes.
    print("\nLambda function examples:")
    square = lambda number: number ** 2
    cube = lambda number: number ** 3
    maximum = lambda first, second: first if first > second else second
    addition = lambda first, second: first + second

    print("Square of 5:", square(5))
    print("Cube of 3:", cube(3))
    print("Maximum of 12 and 8:", maximum(12, 8))
    print("Addition of 12 and 8:", addition(12, 8))


if __name__ == "__main__":
    main()
