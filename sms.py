import vonage
import random

client = vonage.Client(key='65f76cfc', secret='zfNgaDMsd8gagQa8')
sms = vonage.Sms(client)

def send_otp(phone, combined_hex):
    otp = str(random.randint(1000, 9999))
    message = f"Your OTP is: {otp}. Ciphertext: {combined_hex}"
    response = sms.send_message({
        "from": "VonageAPI",
        "to": 254718557081,
        "text": message,
    })
    if response["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response['messages'][0]['error-text']}")
