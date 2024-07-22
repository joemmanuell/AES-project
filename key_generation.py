from Crypto.Random import get_random_bytes

def generate_aes_key(key_size=256):
    return get_random_bytes(key_size // 8)

aes_key = generate_aes_key()
print(f"AES Key: {aes_key.hex()}")
