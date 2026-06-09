# https://en.wikipedia.org/wiki/Programmer

import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    # soup = BeautifulSoup(response.content, "html")

    # print(soup.prettify())
    # print(soup.a)
    # print(soup.find_all("a"))
    # print(soup.find_all("h1"))
    # print(soup.find("material-symbols-rounded"))
    #  print(soup.title.string)

    tag = soup.find_all("a")

    for t in tag:
        url_tags = t.get("href")
        print(url_tags)

    print(tag)


url_input = input("What url would you like to scrape: ")
get_page(url_input)
