import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "Error: At least one character set must be selected!"

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length < 4:
            print("Password length should be at least 4 characters.")
            return

        letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, letters, numbers, symbols)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number for length.")

if __name__ == "__main__":
    main()
