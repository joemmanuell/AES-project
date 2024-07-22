from key_generation import generate_aes_key
from encryption import encrypt_message
from sms import send_otp

aes_key = generate_aes_key()
message = "This is a secure message"
combined = encrypt_message(aes_key, message)
combined_hex = combined.hex()
phone_number = "254718557081"

send_otp(phone_number, combined_hex)
print(f"Combined (IV + Ciphertext): {combined_hex}")
