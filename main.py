import string

alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

index = alphabet.index("a")
upper_index = upper_alphabet.index("A")
def alt_caps(original_string):
    """Convert a string to Alternating Caps

    Args:
        original_string (str): A given string with any kind of capitalization
    Returns:
        str: A new string with alternating capitalization
    Examples:
        >>> print(alt_caps("Alternating Capitalization"))
        aLtErNaTiNg CaPiTaLiZaTiOn
    """
    retcarahc = original_string[0]
    stringdex = original_string.index(retcarahc)
    new_string = ""

    for character in original_string:
        if stringdex % 2 == 0:
            new_character = character.lower()
            new_string += new_character
        elif stringdex % 2 != 0:
            new_character = character.upper()
            new_string += new_character
        stringdex += 1

    # YOUR CODE HERE

    return new_string

print(alt_caps("Why am I doing this"))

