from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    combined = iv + ct_bytes
    return combined

# Example usage
if __name__ == "__main__":
    from key_generation import aes_key

    message = "This is a secure message"
    encrypted_message = encrypt_message(aes_key, message)
    print(f"Combined IV and Ciphertext: {encrypted_message.hex()}")
