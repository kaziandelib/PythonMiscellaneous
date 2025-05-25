import secrets  # Secure random number generator for cryptographic use
import string   # Contains useful string constants like ascii letters, digits, and punctuation

def generate_password(pass_length=12):
    # Define the sets of characters we want to use in our password:
    letters = string.ascii_letters    # All uppercase and lowercase letters (A-Z, a-z)
    digits = string.digits            # All digits (0-9)
    special_char = string.punctuation # Special characters like !, @, #, $, %, etc.

    # Combine all these characters into one big collection we will pick from
    alphabet = letters + digits + special_char

    # Initialize an empty string where we will build the password
    password = ''
    password_is_strong = False  # Flag to keep track if the password meets our strength criteria

    # Keep generating new passwords until one meets the strength requirements
    while not password_is_strong:
        password = ''  # Reset the password string to empty for each new attempt
        
        # For each position in the password (default length 12)
        for i in range(pass_length):
            # Pick a random character from the alphabet securely and add it to the password
            password += ''.join(secrets.choice(alphabet))

        # Check if password contains at least:
        # - one special character
        # - three or more digits
        # This helps ensure password complexity and strength
        if (any(char in special_char for char in password) and sum(char in digits for char in password) >= 3):
            password_is_strong = True  # Password meets criteria, we can stop generating

    # Return the generated strong password
    return password

# When this script runs directly (not imported), generate and print a strong password
if __name__ == '__main__':
    print(generate_password())
