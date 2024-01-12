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
    parts = [] #initialize empty list; store info that is inside curly bracket
    capturing = False #sets capture to boolean value of false; indicating parser is currently outside curly braces
    capture = "" #initializes empty string capture; used to accumulate characters inside curly braces
    for char in template: #starts loop over each character in input 'template' string
        if capturing: #checks if parser is currently inside curly braces
            if char == "}": #checks if current character is the closing curly brace
                parts.append(capture) #if so, appends accumulated characters inside curly braces to 'parts' list
                stripped_template += char #also adds closing curly to stripped template
                capture = "" #resets 'capture' string for next set of characters inside curly braces
                capturing = False #sets 'capturing' to False; parser now outside curly braces
            else:
                capture += char #if current character is not a closing curly brace, adds character to 'capture' string, accumulating characters inside curly braces
        else:
            stripped_template += char #if parser outside curly braces, adds current character to stripped template
            if char == "{": #if current character is opening curly brace, sets 'capturing' to True; parser now inside curly braces
                capturing = True #loops continues all characters in template are processed; in curly braces
    return stripped_template, tuple(parts) #returns stripped template and tuple of language parts extracted from within curly braces. 'tuple(parts)' ensures parts are returned as immutable tuple

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
