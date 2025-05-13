import random
import string

def generate_numeric(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def generate_alphabetic(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def generate_alphanumeric(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def display_menu():
    print("\n--WELCOME--")
    print("="*30)
    print("   PASSWORD GENERATOR")
    print("="*30)
    print("1. Numeric")
    print("2. Alphabetic")
    print("3. Alphanumeric")
    print("4. Exit")

def get_valid_choice():
    try:
        choice = int(input("Enter your choice (1-4): "))
        if choice in [1, 2, 3, 4]:
            return choice
        else:
            print("Invalid option. Please select 1 to 4.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def get_valid_length():
    try:
        length = int(input("Enter the length of the password: "))
        if length > 0:
            return length
        else:
            print("Length must be greater than 0.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

def main():
    while True:
        display_menu()
        choice = get_valid_choice()
        if choice is None:
            continue
        if choice == 4:
            print("Closing...\nGoodBye!")
            break

        length = get_valid_length()
        if length is None:
            continue

        if choice == 1:
            print(f"Your password is: {generate_numeric(length)}")
        elif choice == 2:
            print(f"Your password is: {generate_alphabetic(length)}")
        elif choice == 3:
            print(f"Your password is: {generate_alphanumeric(length)}")

if __name__ == "__main__":
    main()


