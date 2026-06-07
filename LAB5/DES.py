# Parity Drop Table
parity_drop = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
]

# Shift Left Table
shift_table = [
1,1,2,2,2,2,2,2,
1,2,2,2,2,2,2,1
]

# Compression P-Box Table
compression_pbox = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32
]

# Hex to Binary
def hex_to_bin(s):
    return bin(int(s, 16))[2:].zfill(len(s) * 4)

# Binary to Hex
def bin_to_hex(s):
    return hex(int(s, 2))[2:].upper().zfill(len(s)//4)

# Permutation Function
def permute(data, table):
    return "".join(data[i - 1] for i in table)

# Circular Left Shift
def shift_left(data, n):
    return data[n:] + data[:n]

# Generate 16 Round Keys
def generate_round_keys(key_64bit):

    key_56bit = permute(key_64bit, parity_drop)

    left = key_56bit[:28]
    right = key_56bit[28:]

    round_keys = []

    for shift in shift_table:

        left = shift_left(left, shift)
        right = shift_left(right, shift)

        combined = left + right

        round_key = permute(combined, compression_pbox)

        round_keys.append(round_key)

    return round_keys

# Main Program
key_hex = input("Enter 16-digit hexadecimal key: ")

key_64bit = hex_to_bin(key_hex)

round_keys = generate_round_keys(key_64bit)

print("\n16 Round Keys:\n")

for i in range(16):
    print("Round", i + 1, ":", bin_to_hex(round_keys[i]))
