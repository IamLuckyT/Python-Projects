import secrets                # Import the secrets module for generating cryptographically secure random numbers
import string                 # Import the string module for string constants (letters, digits, punctuation)

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """Generate a random password with specified criteria."""
    if length < 1:                                                                             # Check if the requested password length is valid
        raise ValueError("Password length must be at least 1 character.")                      # Raise error if length is less than 1

    characters = string.ascii_lowercase                                                        # Start with lowercase letters as the base character set
    if use_uppercase:                                                                          # If uppercase letters are requested
        characters += string.ascii_uppercase                                                   # Add uppercase letters to the character set
    if use_digits:                                                                             # If digits are requested
        characters += string.digits                                                            # Add digits to the character set
    if use_special_chars:                                                                      # If special characters are requested
        characters += string.punctuation                                                       # Add punctuation to the character set

    if not characters:                                                                         # If no character types are selected
        raise ValueError("At least one character type must be selected.")                      # Raise error

    password = ''.join(secrets.choice(characters) for _ in range(length))                      # Randomly select characters to form the password
    return password                                                                            # Return the generated password

if __name__ == "__main__":                                                                     # If this script is run directly
    # Example usage
    print("Generated Passwords are shown below")
    print("Generated Password:", generate_password())                                          # Generate a default 12-character password with all character types
    print("Generated Password with 16 Characters:", generate_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True))  # Generate a 16-character password with all character types
    print("Generated Password with 8 Characters:", generate_password(length=8, use_uppercase=False, use_digits=False, use_special_chars=False))  # Generate an 8-character password with only lowercase letters
    print("Generated Password with 12 Characters:", generate_password(length=12, use_uppercase=True, use_digits=False, use_special_chars=True))  # Generate a 12-character password with uppercase and special characters only