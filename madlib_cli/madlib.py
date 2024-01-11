import os
import sys

def read_template(path):
    """
    Reads a template file and returns the stripped text.

    :param path: Path to the template file.
    :return: Stripped text content of the template file.
    """
    try:
        with open(path) as file:
            contents = file.read()
            return contents.strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file not found at {path}.")

def parse_template(template):
    """
    Parses a template string and returns a stripped template and a tuple of language parts.

    :param template: Template string with placeholders.
    :return: Stripped template string, tuple of language parts.
    """
    stripped_template = "" #initializes empty string; store modified template without curly braces
    parts = [] #where store info that is inside curly bracket
    capturing = False #outside curly braces
    capture = "" 
    for char in template:
        if capturing:
            if char == "}":
                parts.append(capture)
                stripped_template += char
                capture = ""
                capturing = False
            else:
                capture += char
        else:
            stripped_template += char
            if char == "{":
                capturing = True #inside curly braces
    return stripped_template, tuple(parts)

def merge(stripped_template, parts):
    """
    Merges a stripped template and user-entered language parts.

    :param stripped_template: Stripped template string.
    :param parts: List of user-entered language parts.
    :return: Completed Madlib string.
    """
    return stripped_template.format(*parts)

def main():
    print("Welcome to the Madlib game!")

    template_path = input("Enter the path to the Madlib template file: ")
    stripped_template = read_template(template_path)

    template_parts, language_parts = parse_template(stripped_template)

    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter a {part}: ")
        user_inputs.append(user_input)

    completed_madlib = merge(template_parts, user_inputs)

    print("\nCompleted Madlib:")
    print(completed_madlib)

    output_file_path = input("\nEnter the path to save the completed Madlib: ")
    with open(output_file_path, 'w') as output_file:
        output_file.write(completed_madlib)

if __name__ == "__main__":
    main()
