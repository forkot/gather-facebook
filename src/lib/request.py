import requests

def request(method, url, **kwargs):
    try:
        return requests.Session().request(method, url, **kwargs)
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
        return request(method, url, **kwargs)
