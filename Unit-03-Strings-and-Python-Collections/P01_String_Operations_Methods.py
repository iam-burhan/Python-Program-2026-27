# Unit 3 - Q1: String operations and methods

def main():
    sentence = input("Enter a sentence: ")

    print("\nOriginal sentence:", repr(sentence))
    print("Length:", len(sentence))
    print("Uppercase:", sentence.upper())
    print("Lowercase:", sentence.lower())

    cleaned = sentence.strip()
    print("Without leading/trailing spaces:", cleaned)

    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the replacement word: ")
    print("After replacement:", cleaned.replace(old_word, new_word))

    character = input("Enter one character to count: ")
    if len(character) == 1:
        print(f"Occurrences of {character!r}:", cleaned.count(character))
    else:
        print("Character count skipped: please enter exactly one character.")

    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")
    print("Starts with prefix:", cleaned.startswith(prefix))
    print("Ends with suffix:", cleaned.endswith(suffix))

    # Concatenation joins strings; repetition repeats a string.
    print("Concatenation:", cleaned + " [Python]")
    print("Repetition:", cleaned * 2)
    print("'Python' is present:", "Python" in cleaned)


if __name__ == "__main__":
    main()
