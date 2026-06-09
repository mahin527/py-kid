## `BeautifulSoup`

`from bs4 import BeautifulSoup` means you are using **BeautifulSoup library**. It is a popular **HTML/XML parser** in Python, which is used for web scraping or extracting data from HTML documents.

---

## 🔑 BeautifulSoup's work
- **Parse HTML**: Converts HTML or XML documents into a tree structure.
- **Find elements**: Elements can be found using tag, class, id, attribute.
- **Extract text**: Easily find the text inside HTML tags.
- **Modify HTML**: You can change the content of the document if you want.
- **Web scraping**: It is most commonly used for collecting information from websites.

---

## 📘 Example

### Basic Parsing
```python
from bs4 import BeautifulSoup

html_doc = "<html><body><h1>Hello Mahin</h1><p>This is a test.</p></body></html>"
soup = BeautifulSoup(html_doc, "html.parser")

print(soup.h1.text) # Hello Mahin
print(soup.p.text) # This is a test.
```

---

### Find by Tag
```python
from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<div class="info">First Div</div>
<div class="info">Second Div</div>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, "html.parser")

divs = soup.find_all("div", class_="info")
for d in divs:
print(d.text)
# Output:
# First Div
# Second Div
```

---

## 📝 Things to remember
- To install BeautifulSoup:
```bash
pip install beautifulsoup4
```
- You can use `"html.parser"`, `"lxml"`, or `"html5lib"` as the parser.
- When scraping the web, you should always follow the website's **robots.txt** and terms of service.

