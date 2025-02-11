def textToBits(text: str) -> str:
    bits = ""
    for char in text:
        bits += format(ord(char), '08b')
    return bits

def rounds(L0: str, R0: str, key: str = '000100110011010001010111011110011001101110111100') -> tuple:
    # Expansion permutation (E table)
    E = [32, 1, 2, 3, 4, 5, 4, 5, 
        6, 7, 8, 9, 8, 9, 10, 11, 
        12, 13, 12, 13, 14, 15, 16, 17, 
        16, 17, 18, 19, 20, 21, 20, 21, 
        22, 23, 24, 25, 24, 25, 26, 27, 
        28, 29, 28, 29, 30, 31, 32, 1]

    # Expand R0 to 48 bits using the E table
    expandedR0 = ''.join(R0[i - 1] for i in E)

    # XOR with the round key
    xorResult = ''.join(str(int(expandedR0[i]) ^ int(key[i])) for i in range(48))

    # S-boxes (simplified example, normally there are 8 S-boxes each with a 6-bit input and 4-bit output)
    S = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]

    # Split the XOR result into 6-bit blocks and apply S-boxes
    sboxOutput = ''
    for i in range(0, 48, 6):
        block = xorResult[i:i+6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        sboxValue = S[row][col]
        sboxOutput += format(sboxValue, '04b')

    # Permutation P (simplified example)
    P = [16, 7, 20, 21, 29, 12, 28, 17, 
        1, 15, 23, 26, 5, 18, 31, 10, 
        2, 8, 24, 14, 32, 27, 3, 9, 
        19, 13, 30, 6, 22, 11, 4, 25]

    # Apply permutation P to the S-box output
    permutedSboxOutput = ''.join(sboxOutput[i - 1] for i in P)

    # XOR with L0 to get R1
    R1 = ''.join(str(int(L0[i]) ^ int(permutedSboxOutput[i])) for i in range(32))
    L1 = R0

    return L1, R1

def des(query: str) -> str: 
    print('Initial Query: ', query)

    bitQuery = textToBits(query)
    print('Bit Query: ', bitQuery)

    # Pad bitQuery to ensure it is 64 bits long
    bitQuery = bitQuery.ljust(64, '0')
    print('Padded Bit Query: ', bitQuery)

    # Initial Permutation
    IP = [58, 50, 42, 34, 26, 18, 10, 2, 
        60, 52, 44, 36, 28, 20, 12, 4, 
        62, 54, 46, 38, 30, 22, 14, 6, 
        64, 56, 48, 40, 32, 24, 16, 8, 
        57, 49, 41, 33, 25, 17, 9, 1, 
        59, 51, 43, 35, 27, 19, 11, 3, 
        61, 53, 45, 37, 29, 21, 13, 5, 
        63, 55, 47, 39, 31, 23, 15, 7]


    permutedQuery = ''.join(bitQuery[i - 1] for i in IP)
    print('\nPermuted Query after initial permutation:- \n', permutedQuery, '\n')

    # Round 1
    L0 = permutedQuery[:32]
    R0 = permutedQuery[32:]
    print('Initial L0 and R0 after splitting:- \n')
    print('L0: ', L0, '    ', end='')
    print('R0: ', R0)

    L, R = '', ''
    for i in range(1, 17):
        L, R = rounds(L0, R0)

        print(f'\nAfter Round {i}:- \n')
        print(f'L{i}: ', L, '    ', end='')
        print(f'R{i}: ', R, '\n')
        L0, R0 = R, L # Swap L0 and R0 for the next round

    # Join L16 and R16
    LR = L + R

    # Final Permutation
    FP = [40, 8, 48, 16, 56, 24, 64, 32, 
        39, 7, 47, 15, 55, 23, 63, 31, 
        38, 6, 46, 14, 54, 22, 62, 30, 
        37, 5, 45, 13, 53, 21, 61, 29, 
        36, 4, 44, 12, 52, 20, 60, 28, 
        35, 3, 43, 11, 51, 19, 59, 27, 
        34, 2, 42, 10, 50, 18, 58, 26, 
        33, 1, 41, 9, 49, 17, 57, 25]

    finalQuery = ''.join(LR[i - 1] for i in FP)
    print('\nFinal Query after final permutation:- \n', finalQuery)

    return finalQuery
    




des("Rajat")