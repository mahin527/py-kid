import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urldefrag

visited_urls = set()


def spider_urls(url, keyword):
    url, _ = urldefrag(url)
    if url in visited_urls:
        return
    visited_urls.add(url)

    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MahinBot/1.0; +https://yourdomain.com/bot)"
        }
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"request failed to: {url} ({e})")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        a_tag = soup.find_all("a")

        urls = set()
        for tag in a_tag:
            href = tag.get("href")
            if href:
                full_url = urljoin(url, href)
                full_url, _ = urldefrag(full_url)
                if full_url.startswith("http"):
                    if keyword.lower() in full_url.lower():
                        urls.add(full_url)

        print(f"Found {len(urls)} unique urls containing '{keyword}' at {url}:")
        for u in urls:
            print(u)
            if u not in visited_urls and len(visited_urls) < 50:
                spider_urls(u, keyword)


url = input("Enter the url you want to scrape: ")
keyword = input("Enter the keyword to search for in the url provided: ")

spider_urls(url, keyword)

# TODO: Handle KeyboardInterrupt Error
