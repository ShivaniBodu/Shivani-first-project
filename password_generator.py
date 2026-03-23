import random
import string
import pyperclip

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 4:
        return "💪 STRONG"
    elif score == 3:
        return "😐 MEDIUM"
    else:
        return "😟 WEAK"

def main():
    print("=" * 40)
    print("   🔐 SMART PASSWORD GENERATOR 🔐")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("\nChoose (1/2/3): ").strip()

        if choice == "1":
            try:
                length = int(input("Password length (8-32): "))
                if not (8 <= length <= 32):
                    print("❌ Length must be between 8 and 32!")
                    continue
            except ValueError:
                print("❌ Please enter a valid number!")
                continue

            upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
            digits = input("Include NUMBERS? (y/n): ").lower() == 'y'
            symbols = input("Include SYMBOLS? (y/n): ").lower() == 'y'

            password = generate_password(length, upper, digits, symbols)
            strength = check_strength(password)

            print(f"\n✅ Your Password: {password}")
            print(f"🔍 Strength: {strength}")

            try:
                pyperclip.copy(password)
                print("📋 Password copied to clipboard!")
            except:
                print("(Install pyperclip to auto-copy: pip install pyperclip)")

        elif choice == "2":
            pwd = input("Enter password to check: ")
            strength = check_strength(pwd)
            print(f"🔍 Strength: {strength}")

        elif choice == "3":
            print("\n👋 Goodbye! Stay safe online!")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
