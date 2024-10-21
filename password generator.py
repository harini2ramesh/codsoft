import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    # Define character sets based on complexity
    if complexity == '1':  # Only letters
        characters = string.ascii_letters
    elif complexity == '2':  # Letters and digits
        characters = string.ascii_letters + string.digits
    elif complexity == '3':  # Letters, digits, and special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity choice!")
        return None
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Main function to drive the password generator
def password_generator():
    print("Password Generator")

    # Input: desired length of the password
    length = int(input("Enter the desired password length: "))

    # Input: desired complexity level
    print("\nSelect password complexity level:")
    print("1. Letters only (lowercase and uppercase)")
    print("2. Letters and digits")
    print("3. Letters, digits, and special characters")

    complexity = input("Enter your choice (1/2/3): ")

    # Generate the password
    password = generate_password(length, complexity)

    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    password_generator()
