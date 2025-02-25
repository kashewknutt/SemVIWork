import random

# function for coprime
def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# function for multiucplicative inverse
def mod_inverse(e, phi):
    d = 0
    x1, x2, y1 = 0, 1, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi, e = e, temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2, x1 = x1, x
        d, y1 = y1, y

    if temp_phi == 1:
        return d + phi
    
# main function
def generate_keypair(p, q):
    n = p * q

    phi = (p - 1) * (q - 1)


    e = random.randrange(1, phi)
    g = coprime(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    numbered_array = [ord(char) for char in plaintext]
    print("Numbered Array: ", numbered_array)
    
    cipher = [(num ** key) % n for num in numbered_array]
    print("Encrypted Array: ", cipher)
    
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 17
    q = 19

    public, private = generate_keypair(p, q)
    print("Public Key: ", public)
    print("Private Key: ", private)

    message = "Rajat"

    encrypted_msg = encrypt(public, message)
    print("Encrypted Message: ", encrypted_msg)

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted Message: ", decrypted_msg)