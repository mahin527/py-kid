import requests
import sys

base_url = "https://dineflow-server.onrender.com/api/v1/"


def loop():
    for word in sys.stdin:
        word = word.strip()  # newline remove
        try:
            res = requests.get(f"{base_url}{word}")

            if res.status_code == 404:
                print(f"404 Not Found: {word}")
                continue

            # try JSON parse
            try:
                data = res.json()
            except ValueError:
                data = res.text

            print("Status:", res.status_code)
            print("Word:", word)
            print("Response:", data)

        except Exception as e:
            print(f"Error for {word}: {e}")


loop()
