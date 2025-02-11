The provided code is an implementation of a simplified version of the Data Encryption Standard (DES) algorithm. Here's a breakdown of the main components:

1. **textToBits(text: str) -> str**:
    - Converts a given text string into its binary representation.

2. **rounds(L0: str, R0: str, key: str) -> tuple**:
    - Performs one round of the DES algorithm.
    - Expands the right half (R0) from 32 bits to 48 bits using an expansion permutation table (E).
    - XORs the expanded R0 with a given key.
    - Applies S-boxes to the result of the XOR operation to reduce it back to 32 bits.
    - Applies a permutation (P) to the S-box output.
    - XORs the result with the left half (L0) to produce the new right half (R1).
    - The new left half (L1) is the previous right half (R0).

3. **des(query: str) -> str**:
    - Main function to perform DES encryption on a given query string.
    - Converts the query string to its binary representation and pads it to 64 bits.
    - Applies an initial permutation (IP) to the padded binary string.
    - Splits the permuted string into two halves (L0 and R0).
    - Performs 16 rounds of the DES algorithm using the `rounds` function.
    - Joins the final left and right halves (L16 and R16) and applies a final permutation (FP).
    - Returns the final encrypted binary string.

You can use this explanation to create a PDF using a text editor or a document processor like Microsoft Word or Google Docs.
