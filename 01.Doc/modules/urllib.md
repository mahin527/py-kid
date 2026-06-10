## `urllib`

**`urllib` is a built-in package in Python that provides various submodules for working with URLs — such as reading data from the web, parsing URLs, handling errors, and respecting robots.txt.** It is mainly used for HTTP request/response and URL manipulation. [Python](https://docs.python.org/3/library/urllib.html)

---

## 🔑 Main submodules of `urllib`
- **urllib.request** → Read data from the web or send requests.
- **urllib.error** → Handle exceptions that may occur during requests.
- **urllib.parse** → Break down the URL into its parts (scheme, netloc, path, query, etc.).
- **urllib.robotparser** → Parse the robots.txt file to understand which URLs can be scraped and which cannot.

---

## 📘 Example

### Reading data from URL
```python
from urllib import request

response = request.urlopen("https://www.example.com")
html = response.read().decode("utf-8")
print(html)
````

---

### Parse the URL
```python
from urllib import parse

url = "https://example.com/search?q=python&lang=en"
parsed = parse.urlparse(url);
print(parsed.scheme) # https
print(parsed.netloc) # example.com
print(parsed.query) # q=python&lang=en
````

---

### Respect robots.txt
```python
from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url("https://www.example.com/robots.txt")
rp.read()
print(rp.can_fetch("*", "https://www.example.com/private/"))
```


```python
from urllib.parse import urljoin

if href:
full_url = urljoin(url, href)
if keyword.lower() in full_url.lower():
urls.append(full_url)
```

**`urljoin(url, href)`**
- `href` is often a relative link (such as `/about` or `../contact`).
- `urljoin` combines the base URL (`url`) and the relative path (`href`) to create an **absolute URL**.
- Example:
```python
urljoin("https://example.com", "/about")
# Output: https://example.com/about
```

`urldefrag` is a built-in function from the `urllib.parse` module used to strip the anchor/fragment identifier (anything starting with the # symbol) from a URL. It splits the URL into two parts: the base URL and the isolated fragment string.
```python
from urllib.parse import urldefrag

url = "https://example.com"

# 1. Unpacking as a tuple
base_url, fragment = urldefrag(url)
print(base_url)  # Output: https://example.com
print(fragment)  # Output: section-two

# 2. Accessing via named attributes
result = urldefrag(url)
print(result.url)       # Output: https://example.com
print(result.fragment)  # Output: section-two
```


## 📝 Things to remember
- `urllib` is a **standard library**, so you don't have to install it separately.
- `urllib` is usually used for simple tasks, but for modern API integration, the [**requests module**](./requests.md) is more popular because its API is simple and flexible.
- It is good practice to respect robots.txt with `urllib.robotparser` when doing web scraping.

