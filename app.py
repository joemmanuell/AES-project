from flask import Flask, request, render_template, redirect, url_for
from key_generation import aes_key
from encryption import encrypt_message
from sms import send_otp
from decryption import decrypt_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        phone = request.form["phone_number"]
        message = request.form["message"]

        encrypted_message = encrypt_message(aes_key, message)
        combined_hex = encrypted_message.hex()

        send_otp(phone, combined_hex)

        return redirect(url_for("receive"))
    return render_template("index.html")

@app.route("/receive", methods=["GET", "POST"])
def receive():
    if request.method == "POST":
        otp = request.form["otp"]
        combined = bytes.fromhex(request.form["ciphertext"])

        iv = combined[:16]
        ciphertext = combined[16:]

        decrypted_message = decrypt_message(aes_key, iv, ciphertext)

        return f"Decrypted message: {decrypted_message}"
    return render_template("receive.html")

if __name__ == "__main__":
    app.run(debug=True)
