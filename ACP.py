import random

def generate_password(length=12, include_special_chars=True):
    # """
    # Generate a random password.
    
    # Parameters:
    #     length (int): The length of the password.
    #     include_special_chars (bool): Whether to include special characters.
        
    # Returns:
    #     str: The generated password.
    # """
    # Define the character sets
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/' if include_special_chars else ''
    
    # Create the character pool
    character_pool = letters + digits + special_chars
    
    if not character_pool:
        raise ValueError("Character pool is empty. Ensure include_special_chars is not False.")
    
    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, include_special_chars)
    print("Generated password:", password)
