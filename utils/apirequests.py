import json

import requests

from data.config import URL


def get_audiobooks_by_author(author):
    url = f"{URL}/api/authors/{author}/audiobooks"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def get_authors():
    url = f"{URL}/api/authors"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def get_book_by_title(title):
    url = f"{URL}/api/audiobooks?title={title}"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        return json.loads(response.text)
    return None
