def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - ord('A' if char.isupper() else 'a') + shift_amount) % 26) + ord('A' if char.isupper() else 'a'))
            result += new_char
        else:
            result += char
    return result

encrypted = caesar_cipher("X2YkYHC7UGIqPAUkeI9AQKBcf19GfmEcfcIxC19FPKMnP3MciT==", -3)
print(encrypted)
