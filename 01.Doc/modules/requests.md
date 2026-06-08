## `requests`

**Python's `requests` module is a popular HTTP library that allows you to easily communicate with web servers — such as sending GET, POST, PUT, DELETE requests and reading response data.** It is most commonly used for API calls, data fetching, authentication, file upload/download, etc. [Requests](https://docs.python-requests.org/en/latest/index.html) [Requests](https://docs.python-requests.org/en/latest/user/quickstart.html) [PyPI](https://pypi.org/project/requests/)

---

## 🔑 Main functions of `requests` module
- **Sending HTTP requests**: Easily send GET, POST, PUT, DELETE, etc. requests.
- **Reading response**: Easily get the status code, headers, text, JSON data of the response from the server.
- **Sending parameters**: Can be sent in the form of a URL query string or POST data dictionary.
- **Authentication**: Supports authentication such as Basic, Digest, OAuth etc.
- **Session management**: Cookies and sessions persist and can be used across multiple requests.
- **File upload/download**: Supports multipart file upload and streaming download.
- **SSL verification**: Verify certificates on HTTPS connections.

---

## 📘 Example

### Simple GET Request
```python
import requests

r = requests.get("https://api.github.com/events")
print(r.status_code) # 200
print(r.text) # response body
````

---

### POST Request
```python
import requests

payload = {"key": "value"}
r = requests.post("https://httpbin.org/post", data=payload)
print(r.json()) # JSON response
````

---

### Passing Parameters
```python
import requests

params = {"q": "python", "page": 2}
r = requests.get("https://httpbin.org/get", params=params)
print(r.url) # https://httpbin.org/get?q=python&page=2
````

---

### Authentication Example
```python
import requests

r = requests.get("https://api.github.com/user", auth=("user", "pass"))
print(r.status_code)
```

---

## 📝 Things to remember
- **You need to install**: `pip install requests`
- It is based on **urllib3**, but provides a much simpler API.
- `requests` is used in almost all types of web API integration.
- Cryptography or advanced networking may require a separate library, but `requests` is sufficient for general web communication.

