#!/usr/bin/python3
"""
This script fetches the status from a given URL using the urllib library.
"""


import urllib.request

url = 'https://intranet.hbtn.io/status'
if url.startswith('https://'):
    url = 'https://alu-intranet.hbtn.io/status'

if __name__ == '__main__':
    with urllib.request.urlopen(url) as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


# import urllib.request

# if __name__ == "__main__":
#     url = "https://alu-intranet.hbtn.io/status"
#     with urllib.request.urlopen(url) as request:
#         print("Body response:")
#         data = request.read()
#         print("\t- type: {}".format(type(data)))
#         print("\t- content: {}".format(data))
#         print("\t- utf8 content: {}".format(data.decode("utf-8")))
