import random

def generate_private_key(prime):
    # Choose a large random number x or y in [0, p-1]
    return random.randint(0, prime - 1)

def generate_public_key(prime, base, private_key):
    # Calculate R1 = g^x mod p or R2 = g^y mod p
    return pow(base, private_key, prime)

def generate_shared_secret(prime, received_public_key, private_key):
    # Calculate K = (R2)^x mod p or (R1)^y mod p
    return pow(received_public_key, private_key, prime)

if __name__ == "__main__":
    p = 23
    g = 5

    # Alice
    x = generate_private_key(p)
    R1 = generate_public_key(p, g, x)

    # Bob
    y = generate_private_key(p)
    R2 = generate_public_key(p, g, y)

    # Shared secret
    K_alice = generate_shared_secret(p, R2, x)
    K_bob = generate_shared_secret(p, R1, y)

    print("Alice's Private Key:", x)
    print("Alice's Public Key:", R1)
    print("Bob's Private Key:", y)
    print("Bob's Public Key:", R2)
    print("Alice's Shared Secret:", K_alice)
    print("Bob's Shared Secret:", K_bob)
    if K_alice == K_bob:
        print("Shared secret successfully established!")
    else:
        print("Shared secrets do not match!")