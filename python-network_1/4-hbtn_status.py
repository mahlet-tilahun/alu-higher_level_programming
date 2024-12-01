#!/usr/bin/python3
"""
script that fetches https://alu-intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
