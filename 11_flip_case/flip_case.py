def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = ''.join(
        char.lower() if char == to_swap.upper() else
        char.upper() if char == to_swap.lower() else
        char
        for char in phrase
    )
    return result

print(flip_case('Aaaaahhh', 'a'))