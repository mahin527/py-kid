## `base64`

**Python's `base64` module is a built-in library used for Base64 encoding and decoding of data.** Base64 is a method of converting binary data (such as images, files, or bytes) into ASCII strings, so that it can be easily sent over text-based media (such as JSON, XML, or email).

---

## 🔑 `base64` module functions
- **Encoding binary data**: Converts bytes to a Base64 string.
- **Decoding Base64 string**: Converts a Base64 string back to its original binary data.
- **Safe data transfer**: Used to send binary data over a network or text-based protocol.
- **File handling**: Encodes images or other files to be stored or sent as text.
- **Authentication headers**: In HTTP Basic Authentication, username:password is Base64 encoded.

---

## 📘 Example

### Encode Example
```python
import base64

text = "Mahin Hasan"
encoded = base64.b64encode(text.encode("utf-8"))
print(encoded) # b'TWFoaW4gSGFzYW4='
````

---

### Decode Example
```python
import base64

encoded = b"TWFoaW4gSGFzYW4="
decoded = base64.b64decode(encoded).decode("utf-8")
print(decoded) # Mahin Hasan
````

---

### File Encode/Decode
```python
import base64

# Encode file
with open("image.png", "rb") as f: 
encoded = base64.b64encode(f.read()) 
print(encoded)

# Decode back to file
with open("decoded.png", "wb") as f:
f.write(base64.b64decode(encoded))
```

---

## 📝 Things to remember
- Base64 is **not encryption**, just encoding. Meaning it does not hide data, just converts it to another format.
- Usually used for **data transfer, storage, authentication**.
- Base64 is not enough for cryptography or security, it only provides transport convenience.

