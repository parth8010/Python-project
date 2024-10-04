import string
import secrets
import sys

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
  
    character_sets = []
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character type must be selected.")

    all_characters = ''.join(character_sets)

    if length < len(character_sets):
        raise ValueError(f"Password length must be at least {len(character_sets)} characters to include all selected character types.")

    password = [secrets.choice(char_set) for char_set in character_sets]

    remaining_length = length - len(password)
    password += [secrets.choice(all_characters) for _ in range(remaining_length)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple Python Password Generator")
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password (default: 12)')
    parser.add_argument('--no-upper', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-lower', action='store_true', help='Exclude lowercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-special', action='store_true', help='Exclude special characters')

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

if __name__ == "__main__":
    main()
