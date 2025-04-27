import random
import string

def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    if length < 4:
        return "Password length should be at least 4."

    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "No character types selected!"

    password = random.choices(character_pool, k=length)
    random.shuffle(password)

    return ''.join(password)

# Example usage
try:
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_symbols)
    print("Generated Password:", password)

except ValueError:
    print("Please enter a valid number for the password length.")
