def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = alphabet.index(letter.lower())
    return number

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.isalpha() == True:
        starting_letter = alphabet_position(char.lower())
        end_letter = starting_letter + rot
        if end_letter > 25:
            new_letter = alphabet[end_letter % 26]
        else:
            new_letter = alphabet[end_letter]
        if char.upper() == char:
            new_letter = new_letter.upper()
        return new_letter
    return char

def encrypt(message, rot):
    encrypted = ''
    for i in message:
        encrypted_letter = rotate_character(i, rot)
        encrypted = encrypted + encrypted_letter
    return encrypted
