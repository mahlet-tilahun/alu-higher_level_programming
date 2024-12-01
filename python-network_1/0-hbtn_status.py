#!/usr/bin/python3
"Module that fetches https://alu-intranet.hbtn.io/status"
import urllib.request


url = "https://intranet.hbtn.io/status"
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status

if __name__ == '__main__':
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))
