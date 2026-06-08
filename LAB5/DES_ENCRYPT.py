# ==========================================
# --- TABLES FOR KEY GENERATION ---
# ==========================================

parity_drop_table = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

shift_left_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

Compression_P_Box_Table = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# ==========================================
# --- TABLES FOR ENCRYPTION ---
# ==========================================

initial_permutation_table = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

final_permutation_table = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

expansion_p_box_table = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

straight_p_box_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

s_boxes = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# ==========================================
# --- GENERAL HELPER FUNCTIONS ---
# ==========================================

def hex_to_bin(str_val):
    """Converts a hexadecimal string to a 64-bit binary string."""
    return bin(int(str_val, 16))[2:].zfill(64)

def bin_to_hex(str_val):
    """Converts a binary string back to a hexadecimal string."""
    return hex(int(str_val, 2))[2:].zfill(len(str_val) // 4).upper()

def permute(data, table):
    """Rearranges bits by referring to a given permutation table."""
    result = ""
    for i in table:
        result += data[i - 1]
    return result

def shift_left(data, n):
    """Performs a circular left shift operation."""
    return data[n:] + data[:n]

def xor(a, b):
    """Performs a bitwise XOR operation between two binary strings."""
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def get_inverse_permutation(perm_table):
    """Calculates the inverse of a given permutation table programmatically."""
    inverse_table = [0] * len(perm_table)
    for index, value in enumerate(perm_table):
        inverse_table[value - 1] = index + 1
    return inverse_table

# ==========================================
# --- KEY GENERATION FUNCTION ---
# ==========================================

def generate_round_keys(key_64bit):
    """Generates 16 round keys (48-bit each) from a 64-bit DES key."""
    cipherkey = permute(key_64bit, parity_drop_table)
    left, right = cipherkey[:28], cipherkey[28:]
    round_keys = []
    
    for i in range(16):
        left = shift_left(left, shift_left_table[i])
        right = shift_left(right, shift_left_table[i])
        merged = left + right
        round_key = permute(merged, Compression_P_Box_Table)
        round_keys.append(round_key)
        
    return round_keys

# ==========================================
# --- DES ENCRYPTION FUNCTIONS ---
# ==========================================

def sbox_substitution(data):
    """Applies S-Box substitution to a 48-bit input to get a 32-bit output."""
    result = ""
    for i in range(8):
        chunk = data[i*6:(i+1)*6]
        row = int(chunk[0] + chunk[5], 2)
        col = int(chunk[1:5], 2)
        val = s_boxes[i][row][col]
        result += bin(val)[2:].zfill(4)
    return result

def des_function(right, round_key):
    """The core f-function operating on the right half of the data."""
    temp = permute(right, expansion_p_box_table)
    xor_res = xor(temp, round_key)
    sbox_res = sbox_substitution(xor_res)
    des_function_res = permute(sbox_res, straight_p_box_table)
    return des_function_res

def des_encrypt(plaintext, round_keys):
    """Executes the full 16-round DES encryption process and prints permutation states."""
    
    # 1. Apply Initial Permutation (IP)
    P = permute(plaintext, initial_permutation_table)
    print(f"[*] State after Initial Permutation (IP):      {bin_to_hex(P)}")
    
    left = P[:32]
    right = P[32:]
    
    for i in range(16):
        des_function_res = des_function(right, round_keys[i])
        temp = xor(left, des_function_res)
        left = right  # swap
        right = temp  # swap
        
    # Last round does not contain the swapper
    merged = right + left
    
    # 2. Apply Final Permutation / Inverse IP (IP^-1)
    C = permute(merged, final_permutation_table)
    print(f"[*] State after Inverse Initial Permutation: {bin_to_hex(C)}")
    
    return C

# ==========================================
# --- MAIN EXECUTION / INPUT HANDLING ---
# ==========================================

if __name__ == "__main__":
    
    # Optional: Demonstrate generating the Inverse Permutation Table
    print("--- Generating Inverse Initial Permutation Table ---")
    generated_inverse_ip = get_inverse_permutation(initial_permutation_table)
    
    for i in range(0, len(generated_inverse_ip), 8):
        row = generated_inverse_ip[i:i+8]
        print(" ".join(f"{num:02d}" for num in row))
        
    if generated_inverse_ip == final_permutation_table:
        print(">> Success: The dynamically generated Inverse IP matches the hardcoded Final Permutation table!\n")

    # Task 6 (Objective 1): Key Handling & Round Key Generation
    key = input('Enter key in hex: ')
    key_64bit = hex_to_bin(key)
    round_keys = generate_round_keys(key_64bit)
    
    print("\n--- Generated Round Keys ---")
    for i in range(len(round_keys)):
        print(f"Round Key {i+1} = {bin_to_hex(round_keys[i])}")
        
    # Task 6 (Objective 2): Plaintext Encryption
    print("\n--- DES Encryption ---")
    plaintext_hex = input("Enter plaintext in hex (multiple of 16 hexadecimal digits):\n")
    P_bin = hex_to_bin(plaintext_hex)
    
    # Call the encryption method that includes the printing of states
    print("\n--- Processing ---")
    C_bin = des_encrypt(P_bin, round_keys)
    C = bin_to_hex(C_bin)
    
    print(f"\nFinal Ciphertext: {C}")
