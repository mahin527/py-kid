import base64


def encrypt(input_text):
    encoded_bytes = base64.b64encode(input_text.encode("utf-8"))
    # return encoded_bytes
    print(encoded_bytes.decode())


user_pass = input("Enter your text: ")

encrypt(user_pass)
