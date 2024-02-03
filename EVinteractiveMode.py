import re

def validate_email(email):
    # Define the regex pattern for a valid email address
    pattern = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Replace dashes with empty string
    email_without_dashes = email.replace('-', '')

    # Check if the modified email matches the pattern
    if re.match(pattern, email_without_dashes):
        return True
    else:
        return False

# Example usage
email_input = input("Enter email address in dash mode: ")
if validate_email(email_input):
    print("Valid email address!")
else:
    print("Invalid email address.")