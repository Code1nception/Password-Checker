import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Length (min 8 characters)": length_error,
        "Digit": digit_error,
        "Uppercase letter": uppercase_error,
        "Lowercase letter": lowercase_error,
        "Special character": symbol_error,
    }

    score = sum(not error for error in errors.values())

    if score == 5:
        strength = "Strong"
    elif 3 <= score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, errors

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    strength, errors = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("Details:")
    for criteria, error in errors.items():
        status = "✅" if not error else "❌"
        print(f"{status} {criteria}")

if __name__ == "__main__":
    main()
