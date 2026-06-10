import sys
import requests

out_file = "filtered_urls.txt"


def urls(out_files):
    input_urls = sys.stdin.read().splitlines()

    gd_urls = []
    bd_urls = []

    for url in input_urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                gd_urls.append(url)

        except requests.exceptions.MissingSchema:
            bd_urls.append(url)
            continue

        except requests.ConnectionError:
            bd_urls.append(url)
            continue

    with open(out_file, "w") as file:
        file.write("\n".join(gd_urls))


print(f"Saved URLS {out_file}")

urls(out_file)
