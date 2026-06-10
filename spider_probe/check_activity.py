import sys
import requests


def urls(out_files):
    input_urls = sys.stdin.read().splitlines()

    res_urls = []
    bad_urls = []

    for url in input_urls:
        try:
            pass
        except Exception as e:
            print(e)


out_file = "filtered_urls.txt"
urls(out_file)
