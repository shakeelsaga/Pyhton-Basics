def collatz(number):
    if number == 1:
        return
    
    if number % 2 == 0:
        print(number // 2)
        return collatz(number // 2)
    else:
        print(number * 3 + 1)
        return collatz(number * 3 + 1)

print("Welcome to the Collatz Sequence Calculator!")
print("This program will compute the Collatz sequence for a given number.\n")  
num = int(input("Enter a number: "))
collatz(num)
print("\nThank you for using the Collatz Sequence Calculator!")