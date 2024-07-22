from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_message(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt.decode('utf-8')

if __name__ == "__main__":
    from key_generation import generate_aes_key
    from encryption import encrypt_message
    aes_key = generate_aes_key()
    message = "This is a secure message"
    iv, ciphertext = encrypt_message(aes_key, message)
    decrypted_message = decrypt_message(aes_key, iv, ciphertext)
    print(f"Decrypted Message: {decrypted_message}")
