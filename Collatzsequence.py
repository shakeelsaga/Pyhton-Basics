def collatz(number):
    if number == 1:
        return
    
    if number % 2 == 0:
        print(number // 2)
        return collatz(number // 2)
    else:
        print(number * 3 + 1)
        return collatz(number * 3 + 1)
if __name__ == "__main__":
    print("Welcome to the Collatz Sequence Calculator!\n")
    print("Type 'help' for instructions on how to use the program.")

    while True:
        user_input = input("\nPlease enter a positive integer: ").strip().lower()
        if user_input == 'quit':
            print("Exiting the program. Goodbye!")
            break
        if user_input == 'help':
            print("\nTo use this program, enter a positive integer to compute its Collatz sequence.")
            print("Type 'quit' to exit the program at any time.\n")
            continue
        try:
            num = int(user_input)
            if num <= 0:
                raise ValueError("The number must be a positive integer.")
            collatz(num)
        except ValueError as e:
            print(f"Invalid input: {e}")

    print("\nThank you for using the Collatz Sequence Calculator!")