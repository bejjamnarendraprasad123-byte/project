import random
import string

print("------ Advanced Password Generator ------")

# Password length
while True:
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print("Password length should be at least 4.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# User choices
use_upper = input("Include uppercase letters? (y/n): ").lower()
use_lower = input("Include lowercase letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

# Character selection
characters = ""

if use_upper == 'y':
    characters += string.ascii_uppercase

if use_lower == 'y':
    characters += string.ascii_lowercase

if use_numbers == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Check if user selected at least one option
if characters == "":
    print("You must select at least one character type.")
    exit()

# Number of passwords
count = int(input("How many passwords do you want to generate? "))

print("\n------ Generated Passwords ------")

for i in range(count):

    password = []

    # Ensure strong password conditions
    if use_upper == 'y':
        password.append(random.choice(string.ascii_uppercase))

    if use_lower == 'y':
        password.append(random.choice(string.ascii_lowercase))

    if use_numbers == 'y':
        password.append(random.choice(string.digits))

    if use_symbols == 'y':
        password.append(random.choice(string.punctuation))

    # Fill remaining length
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle password
    random.shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    print(f"\nPassword {i+1}: {final_password}")

    # Password strength checker
    strength = "Weak"

    if length >= 12 and use_upper == 'y' and use_lower == 'y' and use_numbers == 'y' and use_symbols == 'y':
        strength = "Strong"

    elif length >= 8:
        strength = "Medium"

    print("Strength:", strength)