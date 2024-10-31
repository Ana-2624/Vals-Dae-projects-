import re
import time

def is_valid_email(email_address):
    """Check if the provided email format is valid."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email_address)

def is_valid_password(password_string):
    """Check if the password meets the specified requirements."""
    return (len(password_string) >= 12 and
            any(char.isdigit() for char in password_string) and
            any(char.isalpha() for char in password_string) and
            any(not char.isalnum() for char in password_string))


def send_verification_email(email_address):
    """Simulate sending a verification email."""
    print(f"Sending verification email to {email_address}...")

def collect_character_customization():
    """Collect character customization options from the user."""
    character_attributes = {
        'skin_color': input("Choose skin color: "),
        'hair_style': input("Choose hair style: "),
        'outfit': input("Choose outfit: "),
        'gender': input("Choose gender: "),
        'accessories': input("Choose accessories: ")
    }
    return character_attributes

def main():
    print("Welcome to the Game!")
    input("Tap anywhere to continue... (Press Enter)")

    user_information = {}
    character_customizations = []

    while True:
        user_choice = input("Do you want to (1) Login or (2) Sign Up? ")

        if user_choice == '1':  # Placeholder for Login
            print("Login functionality not implemented yet.")
            break
        
        elif user_choice == '2':  # Sign Up
            # Email input with validation
            while True:
                email_address = input("Enter your email: ")
                if not is_valid_email(email_address):
                    print("Invalid email format. Please try again.")
                    continue
                user_information['email'] = email_address
                break
            
            # Collect user information
            user_information['name'] = input("Enter your name: ")
            user_information['username'] = input("Enter your username: ")

            # Age input with validation
            while True:
                user_age = input("Enter your age: ")
                if not user_age.isdigit() or int(user_age) < 0:
                    print("Invalid age. Please enter a valid number.")
                    continue
                
                user_information['age'] = int(user_age)
                break

            # Password input with validation
            while True:
                password_string = input("Create a password (must include at least 12 characters, including numbers, letters, and punctuation): ")
                if not is_valid_password(password_string):
                    print("Password does not meet requirements. Please try again.")
                    continue
                
                user_information['password'] = password_string
                break

            # Age restriction check
            if user_information['age'] < 16:
                print("You must be 16 or older to proceed.")
                continue
            
            # Email verification process
            for attempt in range(3):
                send_verification_email(user_information['email'])
                time.sleep(1)  # Simulate delay for sending email
                is_verified = input("Did you receive the verification email? (yes/no): ").strip().lower()
                if is_verified == 'yes':
                    print("Email verified!")
                    break
                else:
                    if attempt < 2:
                        print("Failed to verify. Please check your email or try again in 1 minute.")
                        time.sleep(60)  # Wait before retrying
                    else:
                        print("Too many failed attempts. Returning to sign-up.")
                        break
            
            # Character creation
            print("Time to create your character!")
            character_customizations = collect_character_customization()

            # Tutorial option
            wants_tutorial = input("Do you want a tutorial? (yes/no): ").strip().lower()
            if wants_tutorial == 'yes':
                print("Starting tutorial...")
                print("This is a quick tutorial on how to play the game.")
                print("You can skip sections of the tutorial if you're already familiar with them.")
            
            # Show notifications
            print("Here are your recent notifications:")
            notifications = ["New update available!", "Check your account settings."]
            for notification in notifications:
                print(notification)
            
            print("End of introduction.")
            break

if __name__ == "__main__":
    main()

