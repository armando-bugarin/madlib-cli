def read_template(path):
    """
    takes in a path to a template file
    and returns the stripped text
    """
    
    with open(path) as file:
        contents = file.read()
        return contents.strip()
    
def parse_template(template):
    """"
    Given "It was a {Adjective} and {Adjective} {Noun}."
    Return "It was a {} and {} {}." and ("Adjective", "Adjective", "Noun")
    """


    return "It was a {} and {} {}." ("Adjective", "Adjective", "Noun")

"""

It was a {Adjective} and {Adjective} {Noun}.

"""

def merge(stripped_template, parts):
    return stripped_template.format(*parts)
