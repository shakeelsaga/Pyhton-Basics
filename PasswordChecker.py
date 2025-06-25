def check_password_strength(password):
    if len(password) < 8:
        return False, "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return False, "Weak: Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return False, "Weak: Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return False, "Weak: Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        return False, "Weak: Password must contain at least one special character."
    
    return True, "Strong: Your password is strong."

if __name__ == "__main__":
    print("Hello there! Welcome to the Password Strength Checker.\n"
        "Please follow the instructions to create a strong password.\n")

    while True:
        password = input("Please enter your password: ")
        is_strong, message = check_password_strength(password)
        print(message)
        if is_strong:
            break

    while True:
        confirm_password = input("Please confirm your password: ")
        if confirm_password == password:
            print("Password confirmed successfully!")
            break
        else:
            print("Passwords do not match. Please try again.")

    print("\nThank you for using the Password Strength Checker. Your password is set!")