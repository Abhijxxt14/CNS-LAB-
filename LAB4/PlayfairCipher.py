# Change this matrix according to your key.
# Example key = MONARCHY

key_matrix = [
['M','O','N','A','R'],
['C','H','Y','B','D'],
['E','F','G','I','K'],  # I and J share one cell
['L','P','Q','S','T'],
['U','V','W','X','Z']
]

def find(ch):
    if ch == 'J':
        ch = 'I'

    for r in range(5):
        for c in range(5):
            if key_matrix[r][c] == ch:
                return r, c

def playfair(text, mode):
    result = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        r1, c1 = find(a)
        r2, c2 = find(b)

        if r1 == r2:      # Same row
            result += key_matrix[r1][(c1 + mode) % 5]
            result += key_matrix[r2][(c2 + mode) % 5]

        elif c1 == c2:    # Same column
            result += key_matrix[(r1 + mode) % 5][c1]
            result += key_matrix[(r2 + mode) % 5][c2]

        else:             # Rectangle rule
            result += key_matrix[r1][c2]
            result += key_matrix[r2][c1]

    return result

plaintext = "HELXLO"      # HELLO → HE LX LO

cipher = playfair(plaintext, 1)   # Encryption
print("Encrypted:", cipher)

plain = playfair(cipher, -1)      # Decryption
print("Decrypted:", plain)
