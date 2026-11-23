# Unit 4 - Q5: Command-line arguments
# Example: python P05_Command_Line_Arguments.py 20 5 +

import argparse
import operator


def main():
    parser = argparse.ArgumentParser(
        description="Perform an arithmetic operation on two command-line numbers."
    )
    parser.add_argument("first", type=float, help="First number")
    parser.add_argument("second", type=float, help="Second number")
    parser.add_argument("operation", choices=["+", "-", "*", "/"],
                        help="Arithmetic operator")
    args = parser.parse_args()

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    if args.operation == "/" and args.second == 0:
        parser.error("division by zero is not allowed")

    result = operations[args.operation](args.first, args.second)
    print(f"{args.first} {args.operation} {args.second} = {result}")


if __name__ == "__main__":
    main()
