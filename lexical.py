import re

# Function to identify whether a line is a comment or not
def is_comment(line):
    # Remove leading and trailing whitespace from the line
    line = line.strip()

    # Check if the line starts with a single-line comment marker (// or #)
    if line.startswith('//') or line.startswith('#'):
        return True

    # Check if the line starts with the beginning of a multi-line comment (/* or ''')
    if line.startswith('/*') or line.startswith("'''"):
        # If the line also ends with the end of a multi-line comment (*/) or (''')
        if line.endswith('*/') or line.endswith("'''"):
            return True
        # If not, it's the start of a multi-line comment
        in_multi_line_comment[0] = True
        return True

    # If we're in the middle of a multi-line comment, check if the line ends with the end marker (*/) or (''')
    if in_multi_line_comment[0] and (line.endswith('*/') or line.endswith("'''")):
        in_multi_line_comment[0] = False
        return True

    # If none of the above conditions match, it's not a comment
    return False

# Example input with lines of code and comments
input_text = '''
# This is a single-line comment
x = 5  # This is also a comment
"""
This is a
multi-line
comment
"""
print("Hello, world!")
'''

# Split the input into lines and check each line
lines = input_text.split('\n')
in_multi_line_comment = [False]

for line in lines:
    if is_comment(line):
        print(f'Comment: {line}')
    else:
        print(f'Not a comment: {line}')
