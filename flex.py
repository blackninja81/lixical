import re

# Function to check if a given string is a valid identifier
def is_valid_identifier(identifier):
    # Define a regular expression pattern for a valid identifier
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, identifier) is not None

# Input identifier to be checked
input_identifier = input("Enter an identifier: ")

# Check if the input identifier is valid
if is_valid_identifier(input_identifier):
    print(f"'{input_identifier}' is a valid identifier.")
else:
    print(f"'{input_identifier}' is not a valid identifier.")
