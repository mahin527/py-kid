import base64


def decrypt(input_text):
    try:
        decoded_bytes = base64.b64decode(input_text).decode("utf-8")
        print(decoded_bytes)
    except ValueError:
        print("Invalid Base64 input")


user_pass = input("Enter your text: ")
decrypt(user_pass)
