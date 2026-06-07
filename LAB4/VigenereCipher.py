def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            j += 1
        else:
            result += ch

    return result

###############################################################################
def vigenere_decrypt(cipher, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in cipher.upper():
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
            j += 1
        else:
            result += ch

    return result


text = input("Enter plaintext: ")
key = input("Enter key: ")

cipher = vigenere_encrypt(text, key)
print("Encrypted:", cipher)

plain = vigenere_decrypt(cipher, key)
print("Decrypted:", plain)
