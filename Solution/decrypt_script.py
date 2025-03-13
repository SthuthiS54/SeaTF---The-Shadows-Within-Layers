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

decrypted = caesar_cipher("base_64_encoded_string_with_ROT13_transformation", -3)
print(decrypted)
