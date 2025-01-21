def additive_substitution_encrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

def additive_substitution_decrypt(text, key):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result

name = "Rajat"
key = 3

encrypted_name = additive_substitution_encrypt(name, key)
decrypted_name = additive_substitution_decrypt(encrypted_name, key)

print(f"Original Name: {name}")
print(f"Encrypted Name: {encrypted_name}")
print(f"Decrypted Name: {decrypted_name}")